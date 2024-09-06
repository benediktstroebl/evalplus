
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

    def count_change(arr, start, end):
        if start == end:
            return 0
        if end - start == 1:
            return 1
        if end - start == 2:
            return 2 if arr[start]!= arr[end] else 0
        if arr[start]!= arr[end]:
            return 1 + min(count_change(arr, start + 1, end), count_change(arr, start, end - 1))
        return count_change(arr, start + 1, end - 1)

    return count_change(arr, 0, len(arr) - 1)
