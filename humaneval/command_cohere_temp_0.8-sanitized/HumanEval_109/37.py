def move_one_ball(arr):
    # If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts needed.
    # Initialize with the number of elements in the array - 1 (assuming
    # the last element is the largest and would "bubble up" to its correct
    # position with shifts)
    shifts = len(arr) - 1

    # Iterate over the array and compare the element at the end with
    # the element at the beginning. If they are out of order, decrement
    # the counter.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            shifts -= 1

    # If any shifts were needed at all, it's possible to sort with shifts.
    return shifts >= 0