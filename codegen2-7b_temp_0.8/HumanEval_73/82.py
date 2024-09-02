
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
    if len(arr) <= 1:
        return 0

    arr.sort()
    d = {num: idx for idx, num in enumerate(arr)}

    def two_diffs(left, right):
        diff = left - right
        if diff == 0:
            return diff
        return min(two_diffs(left - 1, right - 1), two_diffs(left, right - 1))

    return min(two_diffs(0, d[arr[0]] - 1), two_diffs(d[arr[-1] + 1], len(arr) - 1))

