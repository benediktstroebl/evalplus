def maximum(arr, k):
    if k == 1: 
        return max(arr)
    arr = sorted(arr)
    return arr[:k]