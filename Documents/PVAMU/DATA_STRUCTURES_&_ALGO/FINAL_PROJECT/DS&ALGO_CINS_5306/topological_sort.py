import random
from collections import defaultdict, deque
import time

# -------------------------------
# Create DAG 
# -------------------------------

# Generate a random Directed Acyclic Graph (DAG) with 1000 nodes and 3000 edges
num_nodes = 1000
num_edges = 3000

# Adjacency list representation of the directed graph
graph = defaultdict(list)
# Track in-degree (number of incoming edges) for each node
in_degree = {node: 0 for node in range(num_nodes)}
# Keep a set of edges to avoid duplicates
edges = set()

# Randomly generate edges (u → v) ensuring u < v to avoid cycles
while len(edges) < num_edges:
    u = random.randrange(num_nodes)
    v = random.randrange(num_nodes)
    # Only add edge if u < v (guarantees acyclicity) and it's not already present
    if u < v and (u, v) not in edges:
        edges.add((u, v))
        graph[u].append(v)       # Add v to u's adjacency list
        in_degree[v] += 1        # Increment in-degree count for v

# -------------------------------
# Kahn’s Topological Sort
# -------------------------------

def topological_sort(graph, in_degree):
    """
    Perform topological sorting on a DAG using Kahn’s algorithm.
    Returns a list of nodes in one valid topological order.
    """
    # Initialize queue with all nodes that have in-degree 0 (no prerequisites)
    queue = deque([node for node, deg in in_degree.items() if deg == 0])
    topo_order = []  # List to record the sorted order

    # Process until there are no nodes left with in-degree 0
    while queue:
        node = queue.popleft()      # Take one node with in-degree 0
        topo_order.append(node)     # Append it to the result

        # For each neighbor (node → neighbor), reduce its in-degree
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If neighbor now has in-degree 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order

# -------------------------------
# Execution & Timing
# -------------------------------

# Copy in_degree so original counts remain intact
start_time = time.time()
sorted_nodes = topological_sort(graph, in_degree.copy())
elapsed_time = time.time() - start_time

# -------------------------------
# Results
# -------------------------------

print(f"Topological sort visited {len(sorted_nodes)} nodes")  
print(f"Execution time: {elapsed_time:.4f} seconds")
print("First 10 nodes in topological order:", sorted_nodes[:10])
