def can_arrange(arr):
    index = -1
    target = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > target:
            target = arr[i]
        elif arr[i] >= target:
            index = i
    
    return index