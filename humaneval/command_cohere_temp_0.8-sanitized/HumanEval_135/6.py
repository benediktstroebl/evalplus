def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    prev = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur >= prev:
            continue
        max_idx = idx
        prev = cur
    return max_idx