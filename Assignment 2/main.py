def find_route(tickets, start):
    from collections import defaultdict, deque
    
    # Create a graph from the tickets
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)
    
    # To make sure we use each ticket only once, we sort the destinations
    for src in graph:
        graph[src] = sorted(graph[src])
    
    # Use a stack to perform DFS
    stack = [start]
    route = []
    
    def dfs(city):
        while graph[city]:
            next_city = graph[city].pop(0)
            dfs(next_city)
        route.append(city)
    
    dfs(start)
    return route[::-1]

# List of tickets
tickets = [
    ("Paris", "Skopje"),
    ("Zurich", "Amsterdam"),
    ("Prague", "Zurich"),
    ("Barcelona", "Berlin"),
    ("Kiev", "Prague"),
    ("Skopje", "Paris"),
    ("Amsterdam", "Barcelona"),
    ("Berlin", "Kiev"),
    ("Berlin", "Amsterdam")
]

# Starting city
start = "Kiev"

# Find the route
route = find_route(tickets, start)
print("Route:", route)





























































