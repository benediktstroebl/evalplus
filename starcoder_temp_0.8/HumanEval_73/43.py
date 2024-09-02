
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
    n = len(arr)
    mid = n // 2
    res = 0
    if n % 2 == 0:
        if arr[mid - 1] < arr[mid]:
            res += arr[mid] - arr[mid - 1]
        if arr[mid] < arr[mid + 1]:
            res += arr[mid + 1] - arr[mid]
    else:
        if arr[mid] < arr[mid + 1]:
            res += arr[mid + 1] - arr[mid]
    if mid - 1 >= 0:
        if arr[mid - 1] > arr[mid]:
            res += arr[mid] - arr[mid - 1]
        if arr[mid] > arr[mid + 1]:
            res += arr[mid + 1] - arr[mid]
    else:
        if arr[mid] > arr[mid + 1]:
            res += arr[mid] - arr[mid + 1]
    return res

