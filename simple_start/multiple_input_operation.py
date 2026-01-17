from math import prod
from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    values: List[int]
    operation: str
    result: str

def process_values(state: AgentState) -> AgentState:
    """
    This function handles multiple inputs and operations.
    """

    if state["operation"] == "+":
        state["result"] = sum(state["values"])
    elif state["operation"] == "*":
        state["result"] = prod(state["values"])

    state["result"] = f"Hi {state["name"]}, your answer is: {state["result"]}"

    return state

graph = StateGraph(AgentState)

graph.add_node("processor", process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

# answers = app.invoke({"name": "Genia", "values": [1,2,3,4,5], "operation": "+"})
# {'name': 'Genia', 'values': [1, 2, 3, 4, 5], 'operation': '+', 'result': 'Hi Genia, your answer is: 15'}
# answers = app.invoke({"name": "Genia", "values": [1,2,3,4,5], "operation": "*"})
# {'name': 'Genia', 'values': [1, 2, 3, 4, 5], 'operation': '*', 'result': 'Hi Genia, your answer is: 120'}