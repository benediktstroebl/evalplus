def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if not even_nodes:
        return []
    min_value = min(even_nodes)
    min_index = even_nodes.index(min_value)
    return [min_value, min_index]