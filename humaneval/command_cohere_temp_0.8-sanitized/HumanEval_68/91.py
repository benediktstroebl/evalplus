def pluck(arr):
    even_nodes = [idx for idx, val in enumerate(arr) if val % 2 == 0]
    if even_nodes:
        min_idx = min(even_nodes)
        return [arr[min_idx], min_idx]
    else:
        return []