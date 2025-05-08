import time 

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': ['J'],
    'I': ['H'],
    'J': []
}

### declare visited and the queue 

visited = []
queue = ['A']


while queue:
    n = queue.pop()    ## for Breadth first search change this to ==> n = queue.pop(0)
    if n not in visited:
        visited.append(n)

        for node in graph[n]:
            queue.append(node)

    # print("queue :", queue)


print("visited :", visited)