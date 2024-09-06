def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    shift = 0

    # Traverse the array from the last element to the first
    for i in range(1, len(arr)):
        # If the current element is greater than the element it is about to replace, it is not possible to sort the array
        if arr[i] > arr[i-1]:
            shift += 1
            if shift > len(arr):
                return False

    # If we have tried shifting every possible amount and the array is still sorted, it is possible
    return True