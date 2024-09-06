def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes:
        # If there are even nodes, return the node with the smallest index
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        # If there are no even nodes, return an empty list
        return []