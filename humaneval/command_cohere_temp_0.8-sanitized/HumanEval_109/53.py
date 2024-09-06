def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of possible shifts
    shifts = 0

    # Iterate through the array and count shifts
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            shifts += 1

    # Return True if it is possible to obtain a non-decreasing array by shifting
    return shifts >= len(arr)