def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Sort the array and remove duplicates
    arr = sorted(set(arr))
    # Calculate the optimal number of shifts
    num_shifts = arr.count(arr[0])
    # Check if it's possible to obtain a non-decreasing array by shifting
    return num_shifts <= len(arr) - 1