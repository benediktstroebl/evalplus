def can_arrange(arr):
    prev = arr[0]
    arrange = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur >= prev:
            arrange = idx
        prev = cur
    return arrange