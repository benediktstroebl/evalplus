def can_arrange(arr):
    n = len(arr)
    if n <= 1:
        return -1
    max_idx = -1
    check_idx = 0
    for idx in range(n-1):
        if arr[idx] > arr[idx+1]:
            max_idx = idx
            check_idx = idx + 1
            break
    if max_idx != -1 and arr[max_idx] >= arr[check_idx]:
        return max_idx
    else:
        return -1