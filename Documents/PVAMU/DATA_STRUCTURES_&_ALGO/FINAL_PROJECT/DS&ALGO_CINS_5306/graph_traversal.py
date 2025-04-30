import random
from collections import defaultdict, deque
import time

# -------------------------------
# Create Graph
# -------------------------------

# Number of nodes and edges in the random graph
num_nodes = 1000
num_edges = 3000

# Use a defaultdict of lists to represent an adjacency list for an undirected graph
graph = defaultdict(list)
# Keep track of added edges to avoid duplicates
edges = set()

# Randomly add edges until we reach the desired count
while len(edges) < num_edges:
    u = random.randrange(num_nodes)
    v = random.randrange(num_nodes)
    # Ensure no self-loops and no duplicate edges
    if u != v and (u, v) not in edges:
        edges.add((u, v))
        # Since the graph is undirected, add both directions
        graph[u].append(v)
        graph[v].append(u)

# -------------------------------
# Breadth-First Search (BFS)
# -------------------------------

def bfs(graph, start):
    """
    Perform BFS on the graph starting from 'start'.
    Returns the list of nodes in the order they were visited.
    """
    visited = set([start])       # Track visited nodes to prevent re-visiting
    queue = deque([start])       # FIFO queue for the frontier
    order = []                   # List to record visitation order

    while queue:
        node = queue.popleft()   # Get next node from the queue
        order.append(node)       # Record visitation

        # Explore all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# -------------------------------
# Depth-First Search (DFS) - Iterative
# -------------------------------

def dfs(graph, start):
    """
    Perform DFS on the graph starting from 'start', using an explicit stack.
    Returns the list of nodes in the order they were visited.
    """
    visited = set()              # Track visited nodes
    stack = [start]              # LIFO stack for the frontier
    order = []                   # List to record visitation order

    while stack:
        node = stack.pop()       # Pop the top of the stack
        if node not in visited:
            visited.add(node)    # Mark as visited
            order.append(node)   # Record visitation

            # Add unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order

# -------------------------------
# Performance Testing
# -------------------------------

start_node = 0                 # Choose node 0 as the starting point

# Time and run BFS
t0 = time.time()
bfs_result = bfs(graph, start_node)
bfs_time = time.time() - t0

# Time and run DFS
t0 = time.time()
dfs_result = dfs(graph, start_node)
dfs_time = time.time() - t0

# -------------------------------
# Results Output
# -------------------------------

print(f"BFS visited {len(bfs_result)} nodes in {bfs_time:.4f} seconds")
print(f"DFS visited {len(dfs_result)} nodes in {dfs_time:.4f} seconds")
print("First 10 nodes in BFS order:", bfs_result[:10])
print("First 10 nodes in DFS order:", dfs_result[:10])
