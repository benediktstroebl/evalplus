
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
    # check for edge cases
    if len(arr) == 0 or len(arr) == 1:
        return 0
    if arr == arr[::-1]:
        return 0

    # sort and set initial values
    arr.sort()
    num_changes = 0
    midpoint = int(len(arr) / 2)

    # iterate through arr
    for i in range(midpoint):
        if arr[i] != arr[len(arr) - 1 - i]:
            num_changes += 1
    return num_changes

