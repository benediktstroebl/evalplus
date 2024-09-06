def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array and remove duplicates
    arr = sorted(set(arr))
    num_shift_needed = arr[-1] - arr[0]

    # If the difference is 0, return True
    if num_shift_needed == 0:
        return True

    # Otherwise, return False
    return False