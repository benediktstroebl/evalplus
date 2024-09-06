def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_index = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            max_index = i
        if arr[i] >= arr[i+1] and i == n-1:
            max_index = -1
    return max_index