def maximum(arr, k):
    if k <= 0:
        return []
    arr_copy = sorted(arr)
    return arr_copy[:k]