def move_one_ball(arr):
    # if the array is empty, it is always possible to obtain a sorted array
    if not arr:
        return True

    # sort the array
    arr.sort()

    # when the sorted array has elements arranged in non-decreasing order, it is possible to obtain
    # the desired configuration through right shifts
    return arr[0] <= arr[1]