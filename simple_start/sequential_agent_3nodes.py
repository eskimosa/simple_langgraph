from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: str
    skills: List[str]
    final: str

def first_node(state: AgentState) -> AgentState:
    """
    This is the first node of our sequence.
    """

    state["final"] = f"{state["name"]}, welcome to the system!"
    return state

def second_node(state: AgentState) -> AgentState:
    """
    This is the second node of our sequence.
    """

    state["final"] = state["final"] + f" You are {state["age"]} years old!"
    return state

def third_node(state: AgentState) -> AgentState:
    """
    This is the third node of the sequence.
    """
    state["skills"] = (", ").join(state["skills"])

    state["final"] = state["final"] + f" You have skills in: {state["skills"]}"
    return state

graph = StateGraph(AgentState)

graph.add_node("first", first_node)
graph.add_node("second", second_node)
graph.add_node("third", third_node)

graph.set_entry_point("first")
graph.add_edge("first", "second")
graph.add_edge("second", "third")
graph.set_finish_point("third")

app = graph.compile()

