
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
    if arr == sorted(arr):
        return 0
    elif arr == sorted(arr, reverse=True):
        return 0
    if len(arr) == 1:
        return 0
    min_diff = 999999
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            if abs(arr[i] - arr[len(arr) - 1 - i]) < min_diff:
                min_diff = abs(arr[i] - arr[len(arr) - 1 - i])
    return min_diff
