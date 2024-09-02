
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
    # This is a simple question - see if you can find a clever solution.
    if len(arr) == 1:
        return 0
    if arr[0] == arr[-1]:
        return min(smallest_change(arr[1:-1]), smallest_change(arr[:-1]))
    return 1 + smallest_change(arr[1:])


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 4
assert smallest_change([2, 1, 2, 1, 2, 1, 2]) == 5
assert smallest_change([2, 1, 2, 1, 2, 1, 2, 1]) == 3
assert smallest_change([1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 4
assert smallest_change([1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1]) == 2
assert smallest_change([1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2]) == 3
