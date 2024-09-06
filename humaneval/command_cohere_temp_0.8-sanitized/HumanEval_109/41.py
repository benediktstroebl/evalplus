def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in the first half of the array.
    # If so, it will be impossible to sort by shifting only once.
    return min(arr) <= arr[len(arr) // 2]