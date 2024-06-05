import heapq

class Graph:
    def _init_(self):
        self.edges = {}
        self.heuristic = {}

    def add_edge(self, start, end, cost):
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append((end, cost))

    def add_heuristic(self, node, value):
        self.heuristic[node] = value

def astar(graph, start, goal):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        #heapq.heappop will return the smallest value from the queue work as prority queue
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.edges[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + graph.heuristic[neighbor]
                #Add D to frontier with priority 3 + heuristic[D] = 3 + 0 = 3.
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return None

def main():
    graph = Graph()

    # Taking input of graph and heuristic values
    num_edges = int(input("Enter the number of edges: "))
    print("Enter edges in the format 'start end cost'")
    for _ in range(num_edges):
        start, end, cost = input().split()
        cost = int(cost)
        graph.add_edge(start, end, cost)

    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter heuristic values in the format 'node heuristic_value'")
    for _ in range(num_nodes):
        node, heuristic = input().split()
        heuristic = int(heuristic)
        graph.add_heuristic(node, heuristic)

    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    path = astar(graph, start_node, goal_node)
    if path:
        print("Optimal Path:", path)
    else:
        print("No path found from {} to {}.".format(start_node, goal_node))

if _name_ == "_main_":
    main()