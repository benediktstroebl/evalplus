def can_arrange(arr):
    prev = arr[0]
    mx = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return mx
        else:
            mx = idx
        prev = cur
    return mx