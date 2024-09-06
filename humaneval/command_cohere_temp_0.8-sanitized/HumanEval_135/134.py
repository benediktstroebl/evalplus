def can_arrange(arr):
    n = len(arr) - 1
    for i in range(n):
        if arr[i] > arr[i+1]:
            return i
    return -1