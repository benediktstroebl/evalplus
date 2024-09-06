def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if even_nodes:
        min_even_node = min(even_nodes)
        min_index = even_nodes.index(min_even_node)
        return [min_even_node, min_index]
    else:
        return []