def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to make the array sorted.
    shifts = 0

    # Traverse the array from the end to the start.
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            # If the current element is smaller than the previous one, it is possible to sort the array.
            return True

        # Otherwise, we need to perform a right shift operation.
        else:
            shifts += 1
            if shifts >= len(arr):
                # If the number of shifts required is greater than or equal to the array's length, it is impossible to sort.
                return False

    # If we reach the start of the array without returning, it is impossible to sort the array with right shifts.
    return False