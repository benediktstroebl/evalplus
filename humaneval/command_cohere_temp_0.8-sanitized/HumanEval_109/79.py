def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shift = 0

    # Traverse the array from the second position to the end, calculating the maximum number of right shifts required
    for i in range(1, len(arr)):
        # Calculate the number of shifts required to move the current element to the first position
        shift = arr[i] - arr[0]
        max_shift = max(max_shift, shift)

    # If the maximum number of right shifts is zero, the array can be sorted with the given operation
    return max_shift == 0