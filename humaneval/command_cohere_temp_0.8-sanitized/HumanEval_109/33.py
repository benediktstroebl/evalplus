def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    
    # Use a counter to keep track of whether a shift could make the array sorted
    shifts_left = len(arr) - 1
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            shifts_left -= 1
            if shifts_left < 0:
                return False
    
    return True