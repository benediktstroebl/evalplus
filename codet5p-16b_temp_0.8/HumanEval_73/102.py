
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

    def helper(arr, changes):
        if not arr:
            return changes
        first, last = arr[0], arr[-1]
        if first == last:
            return helper(arr[1:-1], changes)
        return min(helper(arr[1:], changes+1), helper(arr[:-1], changes+1))

    return helper(arr, 0)


