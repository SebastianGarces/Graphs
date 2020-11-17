from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    queue = Queue()
    queue.enqueue([starting_node])
    len_long_path = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        path_to_curr_node = queue.dequeue()
        curr_node = path_to_curr_node[-1]

        if len(path_to_curr_node) > len_long_path or \
                ((len(path_to_curr_node) == len_long_path and curr_node < earliest_ancestor)):
            len_long_path = len(path_to_curr_node)
            earliest_ancestor = curr_node

        for ancestor in graph.vertices[curr_node]:
            path_to_ancestor = [*path_to_curr_node, ancestor]
            queue.enqueue(path_to_ancestor)

    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 10))
