def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            continue
        elif cur < prev:
            ans = idx
        else:
            prev = cur
    return ans if ans != len(arr) else -1