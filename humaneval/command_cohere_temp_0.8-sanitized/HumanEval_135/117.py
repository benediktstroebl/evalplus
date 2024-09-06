def can_arrange(arr):
    prev = arr[0]
    mx = -1
    for x in arr[1:]:
        if x > prev:
            return mx
        if x <= prev:
            mx = max(mx, x)
        prev = x
    return mx