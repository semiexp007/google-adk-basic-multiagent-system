"""Minimal OpenAI-backed agent for Google ADK (via LiteLLM)."""

import os

from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv(override=True)

def _openai_model_id() -> str:
    model = os.getenv("OPENAI_MODEL") or os.getenv("ADK_OPENAI_MODEL", "gpt-4o-mini")
    if "/" not in model:
        model = f"openai/{model}"
    return model
    
def _model():
    return LiteLlm(model=_openai_model_id())

math_agent = Agent(
    model=_model(),
    name="math_agent",
    description="Handles calculations, algebra, and quantitative reasoning.",
    instruction="You solve math problems step by step. Give the final answer clearly.",
)
writer_agent = Agent(
    model=_model(),
    name="writer_agent",
    description="Drafts and polishes prose: emails, summaries, marketing copy.",
    instruction="You write clear, concise text. Match the user's tone when specified.",
)
root_agent = Agent(
    model=_model(),
    name="coordinator",
    description=(
        "Routes the user to the right specialist. Answers only simple general chat yourself."
    ),
    instruction=(
        "You coordinate specialists. If the user needs math, transfer to math_agent. "
        "If they need writing help, transfer to writer_agent. "
        "For casual greetings or meta questions about the system, answer directly."
    ),
    sub_agents=[math_agent, writer_agent],
)