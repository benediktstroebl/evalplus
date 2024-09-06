def maximum(arr, k):
    arr.sort()
    ind = 0
    for i in range(k-1):
        max_val = arr[i]
        for j in range(ind, len(arr)):
            if arr[j] > max_val:
                max_val = arr[j]
                ind = j
        arr[i] = max_val
    return arr[:k]