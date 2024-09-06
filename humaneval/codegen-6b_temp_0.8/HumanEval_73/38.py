
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
    def _min_changes(arr):
        if not arr:
            return 0
        elif len(arr) == 1:
            return abs(arr[0] - (len(arr) + 1) % 2)
        else:
            first = arr[-1] - arr[0]
            rest = _min_changes(arr[1:-1])
            return min(first, rest) + 1

    return _min_changes(arr)

