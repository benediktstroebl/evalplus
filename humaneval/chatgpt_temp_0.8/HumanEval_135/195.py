def can_arrange(arr):
    n = len(arr)
    max_idx = -1
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            max_idx = i-1
    return max_idx
