def can_arrange(arr):
    prev = arr[0]
    mx = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur < prev:
            mx = idx
        prev = cur
    return mx if mx != -1 else -1