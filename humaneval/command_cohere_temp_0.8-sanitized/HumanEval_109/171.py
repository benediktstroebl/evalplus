def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shifts = 0

    # Iterate through the array and determine the maximum number of right shifts needed
    for i in range(len(arr)-1):
        # Calculate the number of shifts needed to move the current element to the first position
        shifts = arr[i] - i - 1
        # Update the maximum number of shifts needed
        max_shifts = max(max_shifts, shifts)

    # If a permutation exists where the maximum number of shifts is less than or equal to len(arr), return True
    return max_shifts <= len(arr)