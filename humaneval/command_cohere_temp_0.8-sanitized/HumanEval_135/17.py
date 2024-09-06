def can_arrange(arr):
    prev = arr[0]
    index = 0
    for current in arr[1:]:
        if current > prev:
            return -1
        elif current <= prev:
            index += 1
            prev = current
        else:
            continue
    return index