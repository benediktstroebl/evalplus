def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for idx, val in enumerate(arr):
        if val > arr[idx - 1] and idx > max_idx:
            max_idx = idx
    return max_idx