def can_arrange(arr):
    prev = arr[0]
    mx = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > mx:
            mx = cur
        elif cur < prev:
            return idx
        prev = cur
    return -1 if mx == arr[-1] else idx