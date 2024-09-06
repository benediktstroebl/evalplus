def can_arrange(arr):
    prev = arr[0]
    arrange = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        else:
            arrange = idx
            break
        prev = cur
    return arrange if arrange != len(arr) and arr[arrange] <= arr[arrange - 1] else -1