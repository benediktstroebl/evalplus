def can_arrange(arr):
    prev = arr[0]
    max_index = -1
    
    for i in range(1, len(arr)):
        if arr[i] >= prev:
            max_index = i 
        prev = arr[i]
    
    return max_index