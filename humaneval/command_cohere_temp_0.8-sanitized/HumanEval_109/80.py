def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array and remove duplicates
    arr = sorted(set(arr))
    
    # Check if the sorted array can be created by shifting
    return arr == list(range(len(arr)))