def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        return []