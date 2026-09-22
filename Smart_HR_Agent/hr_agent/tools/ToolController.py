from langchain_core.tools import ToolException
from loguru import logger

from hr_agent.tools.AvailabilityTool import AvailabilityTool
from hr_agent.tools.CalendarTool import CalendarTool
from hr_agent.tools.HCM_Integration.CreateMeeting import MintCreateMeetingTool
from hr_agent.tools.HCM_Integration.CreateRecord import MintCreateRecordTool
from hr_agent.tools.HCM_Integration.CreateRelationships import MintCreateRelTool
from hr_agent.tools.HCM_Integration.DeleteRecord import MintDeleteRecordTool
from hr_agent.tools.HCM_Integration.DeleteRelationships import MintDeleteRelTool
from hr_agent.tools.HCM_Integration.GetModuleFields import MintGetModuleFieldsTool
from hr_agent.tools.HCM_Integration.GetModuleNames import MintGetModuleNamesTool
from hr_agent.tools.HCM_Integration.GetRelationships import MintGetRelTool
from hr_agent.tools.HCM_Integration.GetUsers import MintGetUsersTool
from hr_agent.tools.HCM_Integration.Search import MintSearchTool
from hr_agent.tools.HCM_Integration.UpdateFields import MintUpdateFieldsTool


def _handle_tool_error(error: ToolException) -> str:
    # find if what was returned contains phrase "Module ... does not exist"
    if "does not exist" in error.args[0]:
        logger.error(f"Agent was trying to use module, which does not exist. {error}")
        return f"Module Error: {error} . Try to use MintGetModuleNamesTool to get list of available modules."
    else:
        logger.error(f"The following error occurred during tool execution: {error}")
        return (
            "The following errors occurred during tool execution:"
            + error.args[0]
            + "Please try another tool."
        )


class ToolController:
    available_tools = {
        "MintGetModuleNamesTool": MintGetModuleNamesTool(
            handle_tool_error=_handle_tool_error
        ),
        "MintGetModuleFieldsTool": MintGetModuleFieldsTool(
            handle_tool_error=_handle_tool_error
        ),
        "MintSearchTool": MintSearchTool(handle_tool_error=_handle_tool_error),
        "MintCreateRecordTool": MintCreateRecordTool(
            handle_tool_error=_handle_tool_error
        ),
        "MintCreateMeetingTool": MintCreateMeetingTool(
            handle_tool_error=_handle_tool_error
        ),
        "MintGetUsersTool": MintGetUsersTool(handle_tool_error=_handle_tool_error),
        "UpdateFieldsTool": MintUpdateFieldsTool(handle_tool_error=_handle_tool_error),
        "MintCreateRelTool": MintCreateRelTool(handle_tool_error=_handle_tool_error),
        "MintDeleteRecordTool": MintDeleteRecordTool(
            handle_tool_error=_handle_tool_error
        ),
        "MintDeleteRelTool": MintDeleteRelTool(handle_tool_error=_handle_tool_error),
        "MintGetRelTool": MintGetRelTool(handle_tool_error=_handle_tool_error),
        "CalendarTool": CalendarTool(name="CalendarTool"),
        "AvailabilityTool": AvailabilityTool(),
    }

    default_tools = [
        "MintGetModuleNamesTool",
        "MintGetModuleFieldsTool",
        "MintSearchTool",
        "MintCreateRecordTool",
        "MintCreateMeetingTool",
        "MintGetUsersTool",
        "UpdateFieldsTool",
        "MintCreateRelTool",
        "MintDeleteRecordTool",
        "MintDeleteRelTool",
        "MintGetRelTool",
        "CalendarTool",
        "AvailabilityTool",
    ]

    safe_tools = [
        "CalendarTool",
    ]

    @staticmethod
    def get_available_tools():
        return ToolController.available_tools

    @staticmethod
    def get_default_tools():
        return ToolController.default_tools

    @staticmethod
    def get_safe_tools():
        return ToolController.safe_tools

    @staticmethod
    def get_tools():
        available_tools = ToolController.get_available_tools()
        default_tools = ToolController.get_default_tools()
        return [available_tools[tool] for tool in default_tools]
