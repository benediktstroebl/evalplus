def can_arrange(arr):
    result = -1
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            result = max(result, i)
    return result