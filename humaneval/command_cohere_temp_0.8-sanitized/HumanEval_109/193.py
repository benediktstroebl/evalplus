def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array in place and return the sorted flag
    arr.sort()
    return arr == sorted(arr)
arr = [3, 4, 5, 1, 2]