def can_arrange(arr):
    prev = arr[0]
    index = 0
    for num in arr[1:]:
        if num > prev:
            return -1
        elif num == prev:
            continue
        else:
            prev = num
            index += 1
    return index