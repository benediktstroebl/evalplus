def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_index = -1
    check_index = 0
    while check_index < n:
        if arr[check_index] > arr[check_index-1]:
            max_index = check_index
        check_index += 1
    return max_index