def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr):
        if cur > prev:
            return -1
        if cur <= prev and idx > 0 and arr[idx - 1] < arr[idx]:
            continues = can_arrange(arr[idx:])
            if continues != -1:
                return continues + idx
        if idx == 0:
            arranges.append(idx)
        prev = cur
    if arr[-1] <= arr[-2]:
        return arranges[-1]
    return -1