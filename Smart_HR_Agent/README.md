# Smart HR AI Assistant

A powerful, AI-driven Human Resources Assistant built with LangGraph and Python. This agent is capable of reasoning through complex HR tasks and integrating seamlessly with HCM (Human Capital Management) systems to automate workflows.

## Features
- **Conversational HR Agent**: Understands natural language requests regarding employee data, schedules, and meetings.
- **HCM Integration**: Uses a suite of dynamic tools to fetch, update, and manage records in Human Capital Management systems.
- **LangGraph Architecture**: Built on state-of-the-art graph-based agent loops for robust reasoning and execution.
- **Tool Permitting & Security**: Ensures destructive actions (like deleting records) require confirmation.

## Installation

1. Make sure you have Python 3.10+ installed.
2. Install dependencies via poetry:
   ```bash
   poetry install
   ```

## Configuration
Copy `.env_example` to `.env` and fill in your API keys (e.g., OpenAI/Anthropic) and HCM credentials.

## Usage
Run the agent server:
```bash
poetry run python hr_agent/server.py
```
Or interact with the assistant directly via code:
```python
from hr_agent.HRAssistant import HRAssistant
agent = HRAssistant()
agent.chat("Schedule a meeting with the engineering team.")
```

## Architecture
The core logic resides in `hr_agent/`. Tools for interacting with HR APIs are located in `hr_agent/tools/HCM_Integration`.
