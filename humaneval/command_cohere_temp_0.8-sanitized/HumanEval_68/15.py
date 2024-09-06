def pluck(arr):
    # Filter even nodes and sort by value and index
    even_nodes = [(node, i) for i, node in enumerate(arr) if node % 2 == 0]
    if even_nodes:
        return min(even_nodes, key=lambda x: x[1])
    else:
        return []