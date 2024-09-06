def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array
    arr.sort()
    
    # If the sorted array is equal to the original array, return True
    if arr == sorted(arr):
        return True

    return False