def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to make the array sorted.
    shifts = 0

    # Iterate through the array and count the number of shifts required for each element.
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            shifts += 1
            if shifts > len(arr):
                return False

    # If the total number of shifts is zero, the array is already sorted.
    return shifts == 0