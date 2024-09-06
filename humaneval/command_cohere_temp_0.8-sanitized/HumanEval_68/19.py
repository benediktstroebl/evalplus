def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    return [min(even_nodes), even_nodes.index(min(even_nodes))] if even_nodes else []