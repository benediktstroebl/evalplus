def can_arrange(arr):
    prev = arr[0]
    mx = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur >= prev:
            return -1
        if cur > mx:
            mx = cur
        prev = cur
    return idx if mx != arr[idx] else -1