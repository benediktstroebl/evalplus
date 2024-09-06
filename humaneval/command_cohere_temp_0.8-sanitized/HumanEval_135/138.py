def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        prev = cur
        ans = idx
    return -1 if ans == 0 else ans