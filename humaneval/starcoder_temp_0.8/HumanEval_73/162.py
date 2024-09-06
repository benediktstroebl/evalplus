
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
    n = len(arr)
    res = n
    for i in range(n):
        if i > 0 and arr[i] < arr[i - 1]:
            res -= 1
        if i < n - 1 and arr[n - 1 - i] < arr[n - i]:
            res -= 1
    return res
