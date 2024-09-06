
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    if len(arr) < 2:
        return 0

    forward = 0
    backward = len(arr) - 1

    if arr[forward] == arr[backward]:
        forward += 1

    changes = 0

    while forward < backward:
        while forward < backward and arr[forward] != arr[backward]:
            changes += 1
            forward += 1

        while forward < backward and arr[forward] == arr[backward]:
            forward += 1
            backward -= 1

    return changes

