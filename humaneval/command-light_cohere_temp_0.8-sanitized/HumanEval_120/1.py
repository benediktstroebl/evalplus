def maximum(arr, k):
    # Sort first k elements in arr
    arr = sorted(arr[:k])
    return arr
arr = [-3, -4, 5]
k = 3