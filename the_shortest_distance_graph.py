import time 


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

### declare distances between different nodes : 
distances = {key:float("inf") for key in graph}
distances['A'] = 0.0
precessesor = {}
### declare visited and the queue 
visited = []
queue = ['A']


while queue:
    n = queue.pop()
    if n not in visited:
        visited.append(n)

        for node in graph[n]:
            new_distance = distances[n] + 1
            if new_distance < distances[node]:
                distances[node] = new_distance
            queue.append(node)



print("distances:", distances)
print("visited : ", visited)