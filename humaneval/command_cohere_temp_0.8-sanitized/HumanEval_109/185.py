def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Sort the array and remove duplicates
    arr = sorted(set(arr))
    # Determine the number of shifts required to sort the array in non-decreasing order
    return len(arr) == 1 or arr[1] - arr[0] <= 1