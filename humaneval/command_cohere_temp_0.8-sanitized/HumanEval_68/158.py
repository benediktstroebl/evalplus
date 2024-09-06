def pluck(arr):
    even_nodes = {} 
    for i, num in enumerate(arr):
        if num % 2 == 0:
            even_nodes[num] = i
    if even_nodes:
        min_val = min(even_nodes.keys())
        return [min_val, even_nodes[min_val]]
    return []