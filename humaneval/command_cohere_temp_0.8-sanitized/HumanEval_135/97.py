def can_arrange(arr):
    res = -1
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            res = max(res, i)
    return res