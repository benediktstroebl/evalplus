def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array.
    shifts = 0

    # Traverse the array from the last element to the first element.
    for i in range(len(arr) - 2, -1, -1):
        # Increment the counter if the current element is smaller than the next element.
        if arr[i] < arr[i + 1]:
            shifts += 1

    # If the number of right shifts is odd, it is possible to sort the array in non-decreasing order.
    return shifts % 2 == 1