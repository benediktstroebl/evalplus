
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
    if len(arr) == 1:
        return 0
    middle = len(arr) / 2
    s1 = smallest_change(arr[:middle])
    s2 = smallest_change(arr[middle:])
    s3 = sum(abs(x - y) for x, y in zip(arr, arr[::-1]))
    return min(s1, s2, s3) + 1

