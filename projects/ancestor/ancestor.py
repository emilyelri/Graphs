from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    g = ancestors_graph(ancestors)

    if len(g.get_neighbors(starting_node)) == 0:
        return -1

    distance = 0
    distances = {}
    
    q = Queue()
    q.enqueue([starting_node, distance])

    while q.size() > 0:
        person, curr_distance = q.dequeue()

        if curr_distance in distances:
            distances[curr_distance].append(person)

        else:
            distances[curr_distance] = [person]

        neighbors = g.get_neighbors(person)
        if len(neighbors) > 0:
            distance += 1
            for relative in neighbors:
                q.enqueue([relative, distance])
    
    farthest = max(distances.keys())
    result = min(distances[farthest])

    return result

def ancestors_graph(ancestors):
    g = Graph()
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        if parent not in g.vertices:
            g.add_vertex(parent)
        if child not in g.vertices:
            g.add_vertex(child)
        g.add_edge(child, parent)
    return g

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
ancestors_graph(test_ancestors)