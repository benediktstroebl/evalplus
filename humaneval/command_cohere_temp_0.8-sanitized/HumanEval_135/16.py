def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return arranged
        elif cur <= prev:
            arranged = idx
        prev = cur
    return arranged