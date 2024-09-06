
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
    left = 0
    right = 0
    res = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            left += 1
        if arr[i] == 2:
            right += 1
        if right == left:
            res = min(res, right - left + 1)
        if arr[i] == 0:
            left = right = 0
    return res
