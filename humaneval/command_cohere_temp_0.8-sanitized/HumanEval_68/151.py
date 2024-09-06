def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if not even_nodes:
        return []
    min_value = min(even_nodes)
    min_index = even_nodes.index(min_value)
    return [min_value, min_index]