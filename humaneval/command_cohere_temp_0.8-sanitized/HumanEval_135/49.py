def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for idx, val in enumerate(arr):
        if idx == 0:
            continue
        if val <= arr[idx - 1]:
            max_idx = idx
            break
    return max_idx