def move_one_ball(arr):
    """
    Determine if the array can be sorted by right shifts.

    Args:
        arr (list): A list of integers with unique elements.

    Returns:
        bool: True if the array can be sorted, False otherwise.
    """
    if not arr:  # Edge case: Empty array
        return True
    
    max_val = max(arr)
    idx = arr.index(max_val)

    # Check if the max value can be moved to the front
    for i in range(idx, -1, -1):
        if arr[i] < max_val:
            return False
    
    return True