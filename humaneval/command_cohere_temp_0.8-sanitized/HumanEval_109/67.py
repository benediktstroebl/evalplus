def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Check if the maximum element in the array can reach the first position after iterating through the array.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return True
    
    return False