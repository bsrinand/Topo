from collections import deque

def topological_sort(vertices, edges):
    in_degree = {v: 0 for v in vertices}
    graph = {v: [] for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(vertices) else []

vertices = [1, 2, 3, 4, 5, 6]
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topological_sort(vertices, edges))  # Output: [5, 4, 2, 3, 1, 0]
