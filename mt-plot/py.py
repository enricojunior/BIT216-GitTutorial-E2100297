import network as nx
import matplotlib.pyplot as plt

# Define activities with duration and their dependencies
activities = {
    'A': {'duration': 2, 'predecessors': []},
    'B': {'duration': 2, 'predecessors': ['A']},
    'C': {'duration': 3, 'predecessors': ['A']},
    'D': {'duration': 4, 'predecessors': ['A']},
    'E': {'duration': 2, 'predecessors': ['B']},
    'F': {'duration': 3, 'predecessors': ['C']},
    'G': {'duration': 6, 'predecessors': ['D']},
    'H': {'duration': 2, 'predecessors': ['E', 'F']},
    'I': {'duration': 5, 'predecessors': ['E', 'F']},
    'J': {'duration': 1, 'predecessors': ['I']},
    'K': {'duration': 2, 'predecessors': ['H', 'J']}
}

# Create directed graph for PDM
G = nx.DiGraph()

# Add nodes and edges based on activities and dependencies
for activity, data in activities.items():
    G.add_node(activity, duration=data['duration'])
    for pred in data['predecessors']:
        G.add_edge(pred, activity)

# Plotting the PDM
pos = nx.planar_layout(G)  # planar layout for better visual structure
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): '' for u, v in G.edges()})
plt.title("Project Dependency Model (PDM)")
plt.show()
