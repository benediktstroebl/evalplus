def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of possible shifts
    shifts = 0

    # Traverse through the array
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            shifts += 1
            if shifts > len(arr) - 1:
                return False

    return True