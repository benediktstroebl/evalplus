def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for idx, cur in enumerate(arr[1:]):
        if cur > prev:
            continue
        elif cur < prev:
            ans = idx + 1
        else:
            prev = cur
    return max(ans, -1)