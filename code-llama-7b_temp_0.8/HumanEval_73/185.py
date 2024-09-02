
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
    if not arr:
        return 0

    n = len(arr)
    if n == 1:
        return 0

    if n == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1

    # Find the middle of the array
    mid = n//2

    # Find the sub-arrays
    left = arr[:mid]
    right = arr[mid:]

    # Fix left and right sub-arrays
    for i in range(mid):
        left[i] = right[i]

    # The minimum of left and right sub-arrays should be the
    # sum of number of changes on left and right sub-arrays
    return min(smallest_change(left), smallest_change(right))

