def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array
    arr.sort()

    # If the sorted array is non-decreasing, return True
    if arr[0] <= arr[1]:
        return True

    # Otherwise, return False
    return False