
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
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
        if arr[mid] != arr[mid - 1]:
            return 1
        if mid - 2 >= 0 and arr[mid - 2] != arr[mid - 1]:
            return 2
        return 0
    mid = len(arr) // 2
    if arr[mid] != arr[mid - 1]:
        return 1
    if mid - 2 >= 0 and arr[mid - 2] != arr[mid - 1]:
        return 2
    return 0
