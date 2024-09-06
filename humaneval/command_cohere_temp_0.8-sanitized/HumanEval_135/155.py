def can_arrange(arr):
    prev = arr[0]
    arranged = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        arranged = idx
        break
    else:
        return -1
    return arranged