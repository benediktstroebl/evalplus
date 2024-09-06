
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
    # write your code in Python 3.6
    if not arr or len(arr) == 0:
        return 0

    start, end = 0, len(arr) - 1
    count = 0

    while start < end:
        if arr[start]!= arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            count += 1
        start += 1
        end -= 1

    return count

