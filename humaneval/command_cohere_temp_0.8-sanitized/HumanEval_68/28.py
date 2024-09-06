def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if even_nodes:
        min_val = min(even_nodes)
        min_index = even_nodes.index(min_val)
        return [min_val, min_index]
    else:
        return []