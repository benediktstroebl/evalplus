def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize the variable should_swap to False
    should_swap = False

    # Iterate over the array
    for i in range(len(arr)):
        # If the current element is greater than the previous one, we should swap
        if arr[i] > arr[i-1] and not should_swap:
            should_swap = True
        # If the current element is smaller than the previous one, we have to reset the flag
        else:
            should_swap = False

    # If the flag is True at the end, it is possible to achieve non-decreasing order
    return should_swap