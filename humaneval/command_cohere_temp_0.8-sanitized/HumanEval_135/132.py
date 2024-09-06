def can_arrange(arr):
    prev = arr[0]
    index = 0
    for num in arr[1:]:
        if num <= prev:
            index += 1
            if num >= arr[index]:
                return index
        else:
            prev = num
    return -1