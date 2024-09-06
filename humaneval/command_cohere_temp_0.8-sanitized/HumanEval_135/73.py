def can_arrange(arr):
    result = -1
    for idx, val in enumerate(arr):
        if arr[idx] > arr[idx - 1]:
            result = idx
            break
    return result