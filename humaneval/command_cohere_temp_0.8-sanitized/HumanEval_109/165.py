def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if len(arr) == 0:
        return True

    # Check if any element exists in the array that is not in the first position
    for i in range(1, len(arr)):
        if arr[i] != arr[0]:
            return True

    return False