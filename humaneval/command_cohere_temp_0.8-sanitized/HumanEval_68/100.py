from collections import defaultdict
def pluck(arr):
    even_nodes = defaultdict(list)
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even_nodes[n].append(i)
    
    if not even_nodes:
        return []

    # If multiple nodes with the same smallest even value, pick the one with the smallest index
    smallest_index = min(idx for val, idx in even_nodes.items() if len(idx) > 1)
    return [min(even_nodes), smallest_index]