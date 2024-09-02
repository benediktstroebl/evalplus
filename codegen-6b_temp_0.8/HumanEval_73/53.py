
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

    last = len(arr) - 1
    mid = last // 2
    while mid > 0:
        if arr[mid] < arr[last - mid]:
            last = mid
            mid = (last - mid) // 2
        else:
            mid = mid // 2

    first = 0
    last = len(arr) - 1
    while first < last:
        if arr[first] > arr[last]:
            return last - first
        if arr[first] < arr[last]:
            first += 1

    return 0
