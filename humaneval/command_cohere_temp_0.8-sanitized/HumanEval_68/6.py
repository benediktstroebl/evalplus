import unittest
def pluck(arr):
    even_nodes = {}
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even_nodes.setdefault(n, []).append(i)
    
    if not even_nodes:
        return []

    min_index = None
    min_value = min(list(even_nodes.keys()))
    for idx in even_nodes[min_value]:
        if min_index is None or idx < min_index:
            min_index = idx
    
    return [min_value, min_index] if min_index is not None else []