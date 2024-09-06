
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
    if arr is None or len(arr) <= 1:
        return 0

    cache = {}

    def smallest_change_helper(arr, index, minimum):
        if index == len(arr) - 1:
            return minimum
        if index in cache:
            return cache[index]

        change = min(smallest_change_helper(arr, index + 1, minimum), smallest_change_helper(arr, index + 2, minimum))
        cache[index] = change + 1
        return change + 1

    return smallest_change_helper(arr, 0, len(arr)
