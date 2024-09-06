def can_arrange(arr):
    result = -1
    for idx, value in enumerate(arr):
        if value > arr[idx-1]:
            result = idx
    return result