def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            max_idx = i
        if arr[i] >= arr[i-1] and i-1 != -1:
            max_idx = i-1
    return max_idx