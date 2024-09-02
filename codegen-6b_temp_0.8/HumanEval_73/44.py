
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
    def is_palindrome(arr):
        return arr[:] == arr[::-1]

    n = len(arr)
    changes = 0

    # if all elements are the same
    if is_palindrome(arr):
        return changes

    for i in xrange(n/2):
        if arr[i] != arr[n-1-i]:
            changes += 1
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

    return changes

assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 4
