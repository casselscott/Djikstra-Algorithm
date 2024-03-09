class Graph:
    def __init__(self):
        self.datalist = {}

    def add_data(self, data):
        if data not in self.datalist:
            self.datalist[data] = []

    def add_edge(self, src, dest, kilometres):
        if src in self.datalist and dest in self.datalist:
            self.datalist[src].append((dest, kilometres))
            self.datalist[dest].append((src, kilometres))

    def get_neighbors(self, data):
        return self.datalist[data]

def dijkstra(graph, start, end):
    # Initialize distances from start node to all other nodes as infinity
    distances= {data: float('inf') for data in graph.datalist}
    distances[start] = 0

    # Initialize an empty dictionary to store the shortest path
    shortest_path = {}

    # Initialize a priority queue to store vertices with their distances from start node
    flightpath_queue = [(0, start)]

    while flightpath_queue:
        current_distance, current_data = min(flightpath_queue)
        flightpath_queue.remove((current_distance, current_data))

        if current_distance > distances[current_data]:
            continue

        for neighbor, kilometres in graph.get_neighbors(current_data):
            distance = current_distance + kilometres
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_data
                flightpath_queue.append((distance, neighbor))

    # Construct the shortest path from start to end
    path = []
    current_data = end
    while current_data != start:
        path.insert(0, current_data)
        current_data = shortest_path[current_data]
    path.insert(0, start)

    return path, distances[end]

# Example usage:
flight_graph = Graph()
flight_graph.add_data("London")
flight_graph.add_data("Belgium")
flight_graph.add_data("Canada")
flight_graph.add_data("Denmark")

flight_graph.add_edge("London", "Belgium", 1600)
flight_graph.add_edge("London", "Canada", 4600)
flight_graph.add_edge("Belgium", "Denmark", 1300)
flight_graph.add_edge("Canada", "Denmark", 6000)

shortest_path, distance = dijkstra(flight_graph, "London", "Denmark")
print("What is the Shortest path:", shortest_path)
print ("Distance in Kilometres:", distance)

    
     
    
            
