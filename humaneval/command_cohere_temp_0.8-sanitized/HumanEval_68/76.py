def pluck(arr):
    even_nodes = [idx for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    min_idx = min(even_nodes)
    min_val = arr[min_idx]
    return [min_val, min_idx]