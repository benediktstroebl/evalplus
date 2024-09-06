def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur <= prev:
            arranges.append(idx)
            prev = cur
    return max(arranges) if arranges else -1