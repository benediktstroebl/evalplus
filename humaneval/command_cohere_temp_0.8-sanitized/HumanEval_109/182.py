def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in the first half of the array.
    index = arr[-1]
    left = 0
    for i in range(len(arr)):
        if arr[i] < index:
            left += 1
        if left > len(arr) // 2:
            return False

    return True