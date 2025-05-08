graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # set to store 'visited'
queue = ['A']    # list to store 'queue'

while queue:  # while queue not empty
    n = queue.pop()  # pick nodes from the right
    if n not in visited:  # if n has not been visited (avoid cycles)
        print(n, end=" ")  # do what needs to be done
        visited.append(n)     # add n to the set of visited
        for child in graph[n]:  # traverse all neighbors
            queue.append(child)  # push to the right of queue

    print("queue", queue)
    print("visited", visited)
    input("press enter to continue ")