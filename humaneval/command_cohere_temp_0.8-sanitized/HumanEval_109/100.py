def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shift = 0

    # Traverse the array from the last element to the first
    for i in range(len(arr) - 2, -1, -1):
        # Calculate the number of right shifts required to move the current element to the first position
        shift = len(arr) - i - 1

        # Update the maximum number of right shifts required for any element
        max_shift = max(max_shift, shift)

        # If the maximum number of right shifts required is greater than the length of the array, it is not possible to sort it in non-decreasing order
        if max_shift > len(arr):
            return False

    return True