def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if even_nodes:
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        return []