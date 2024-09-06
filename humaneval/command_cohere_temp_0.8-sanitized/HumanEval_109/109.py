def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in its correct position in the sorted array.
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return False

    # If all elements are in their correct positions, it is possible to sort by shifting.
    return True