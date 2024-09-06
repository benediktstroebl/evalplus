def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Use a counter to keep track of possible shifts
    shifts = 0

    # Iterate through the array and count shifts
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            shifts += 1

    # Return True if any number of shifts will arrange the array in ascending order
    return shifts >= len(arr) - 1