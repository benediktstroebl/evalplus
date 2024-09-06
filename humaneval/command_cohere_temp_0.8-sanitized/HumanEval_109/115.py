def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array in place and return True if sorted in non-decreasing order
    sorted_arr = sorted(arr)
    return sorted_arr == arr