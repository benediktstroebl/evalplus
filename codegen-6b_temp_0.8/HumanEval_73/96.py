
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
    # if arr is empty
    if len(arr) == 0:
        return 0
    # if arr is already palindromic
    if is_palindrome(arr):
        return 0
    # if arr has only 1 element
    if len(arr) == 1:
        return 0
    # if arr has more than one element
    smallest = float("inf")
    for i in xrange(len(arr)):
        left = smallest_change(arr[:i])
        right = smallest_change(arr[i+1:])
        smallest = min(smallest, left + right)
    return smallest + 1
