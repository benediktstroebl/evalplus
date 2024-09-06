def can_arrange(arr):
    prev = arr[0]
    arranged = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        arranged = idx
        break
    return arranged if arranged != len(arr) and arr[arranged] <= arr[arranged - 1] else -1