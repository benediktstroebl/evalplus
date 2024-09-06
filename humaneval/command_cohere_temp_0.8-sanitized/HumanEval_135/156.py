def can_arrange(arr):
    prev = arr[0]
    index = 0
    for current in arr[1:]:
        if current > prev:
            return -1
        elif current == prev:
            continue
        else:
            prev = current
            index += 1
    return index