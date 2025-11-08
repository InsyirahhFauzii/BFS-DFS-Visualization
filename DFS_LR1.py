import streamlit as st
from collections import deque

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F'],
    'H': ['F', 'G'],
    'F': []
}

st.set_page_config(page_title="DFS Visualizer", layout="centered")
st.title("Depth-First Search (DFS) Visualizer")

st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph", use_container_width=True)

start = st.selectbox("Select the starting node:", sorted(graph.keys()), index=0)

def dfs(node, graph, visited=None, levels=None, level=0, path=None):
    if visited is None:
        visited = []
    if levels is None:
        levels = {}
    if path is None:
        path = []
    visited.append(node)
    levels[node] = level
    path.append(node)
    for neighbor in sorted(graph[node]):
        if neighbor not in visited:
            dfs(neighbor, graph, visited, levels, level + 1, path)
    return visited, levels, path

if st.button("Run DFS"):
    visited, levels, path = dfs(start, graph)
    st.subheader("Traversal Order:")
    st.write("DFS Traversal Order:", " -> ".join(path))
    st.subheader("Node Discovery Level:")
    for node in path:
        st.info(f"Level {levels[node]} -> {node}")

