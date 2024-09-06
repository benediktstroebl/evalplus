def move_one_ball(arr):
    # if the array is empty, it is always possible to obtain a sorted array
    if not arr:
        return True

    # sort the array
    arr.sort()

    # when the sorted array has elements arranged in non-increasing order, it is possible to obtain a non-decreasing order with right shifts
    if arr[0] >= arr[1]:
        return True

    return False