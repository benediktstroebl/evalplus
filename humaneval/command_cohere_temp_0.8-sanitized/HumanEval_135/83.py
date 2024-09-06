def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            max_idx = idx
            prev = cur
    return max_idx