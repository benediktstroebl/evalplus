
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

    # Find the palindromic length of the array
    mid = len(arr) // 2
    for i in range(mid):
        if arr[i] != arr[len(arr) - i - 1]:
            break
    n = len(arr) - i - 1

    # Find the required number of changes
    count = 0
    for i in range(mid, n):
        if arr[i] != arr[i - mid]:
            count += 1
    return count
