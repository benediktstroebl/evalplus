def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if len(arr) == 0:
        return True

    # Use a flag to track if a pass through the array results in a non-decreasing order
    is_sorted = False

    # Attempt to move the last ball to the first position by shifting the array
    for _ in range(len(arr)):
        # Swap the first element with the last element after each shift
        if arr[0] > arr[-1]:
            arr[0], arr[-1] = arr[-1], arr[0]
        # If the first element is less than or equal to the second element, the array is sorted
        if arr[0] <= arr[1]:
            is_sorted = True
            break

    # If a single pass through the array does not result in a sorted array, return False
    return is_sorted