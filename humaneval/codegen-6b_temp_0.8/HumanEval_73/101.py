
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
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        mid -= 1
    change = 0
    if arr[mid] != arr[mid + 1]:
        change += 1
        return smallest_change(arr[:mid]) + smallest_change(arr[mid + 2:]) + 1
    return change + smallest_change(arr[:mid]) + smallest_change(arr[mid + 1:])

