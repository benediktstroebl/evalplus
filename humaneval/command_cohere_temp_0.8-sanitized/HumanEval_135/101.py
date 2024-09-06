def can_arrange(arr):
    prev = arr[0]
    index = 0
    for curr in arr[1:]:
        if curr <= prev:
            index += 1
            prev = curr
        else:
            break
    return index if index < len(arr) else -1