def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes:
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        return []