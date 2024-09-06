def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Use a counter to keep track of possible shifts
    shifts = 0

    # Iterate through the array and count shifts
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            shifts += 1

    # If shifts is greater than or equal to the length of the array, it's possible to sort
    return shifts >= len(arr)