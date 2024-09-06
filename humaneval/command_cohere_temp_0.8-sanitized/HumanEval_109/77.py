def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if the input array is of size 1, 2 or 3 to optimize the resolution.
    # If so, a comparison to the first element of the array after a right shift
    # will determine if it is possible to sort the array in non-decreasing order.
    if len(arr) in [1, 2, 3]:
        return arr[0] >= arr[1]

    # We assume it is not possible to sort the array in non-decreasing order after
    # a right shift if the first two elements of the array do not compare correctly.
    if arr[0] > arr[1]:
        return False

    # We perform up to len(arr) right shifts, comparing the first element after
    # each shift to the current last element in the array. If any of these comparisons
    # are true, we return False, assuming it is not possible to sort the array in
    # non-decreasing order.
    for _ in range(len(arr)):
        if arr[0] >= arr[-1]:
            return False

    return True