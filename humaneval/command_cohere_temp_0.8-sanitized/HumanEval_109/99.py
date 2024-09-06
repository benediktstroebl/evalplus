def move_one_ball(arr):
    # Base case: If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Sort the array in place using sorting indices.
    sorting_idx = [i for i in range(len(arr))]
    sorting_idx.sort(key=lambda i: arr[i])
    
    # If the sorted array is non-decreasing, return True.
    for i in range(len(arr)):
        if arr[sorting_idx[i]] < arr[i]:
            return True
    
    # If all elements are equal, it's still possible to sort the array.
    if len(set(arr)) == 1:
        return True
    
    # Otherwise, it's not possible to sort the array by moving one ball.
    return False