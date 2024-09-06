def pluck(arr):
    # Insert even nodes into a sorted list
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes:
        sorted_nodes = sorted(even_nodes)
        return [sorted_nodes[0], even_nodes.index(sorted_nodes[0])]
    return []