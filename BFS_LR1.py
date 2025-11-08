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

st.set_page_config(page_title="BFS Visualizer", layout="centered")
st.title("Breadth-First Search (BFS) Visualizer")

st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph", use_container_width=True)

start = st.selectbox("Select the starting node:", sorted(graph.keys()), index=0)

def bfs(node, graph):
    visited = []
    levels = {}
    path = []
    queue = deque()
    queue.append((node, 0))
    while queue:
        current, level = queue.popleft()
        if current not in visited:
            visited.append(current)
            levels[current] = level
            path.append(current)
            for neighbor in sorted(graph[current]):
                if neighbor not in visited and neighbor not in [item[0] for item in queue]:
                    queue.append((neighbor, level + 1))
    return visited, levels, path

if st.button("Run BFS"):
    visited, levels, path = bfs(start, graph)
    st.subheader("Traversal Order:")
    st.write("BFS Traversal Order:", " -> ".join(path))
    st.subheader("Node Discovery Level:")
    for node in path:
        st.info(f"Level {levels[node]} → {node}")
