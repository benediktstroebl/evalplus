def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Sort the array and remove duplicates
    arr = sorted(set(arr))
    # Determine the number of shifts required to sort the array in non-decreasing order
    shifts = sum(1 for i in range(1, len(arr)) if arr[i] >= arr[i-1])
    # Return False if it is not possible to achieve non-decreasing order with right shifts
    return shifts == 0