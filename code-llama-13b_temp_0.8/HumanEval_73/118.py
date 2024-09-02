
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
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0

    # The first element is odd
    if len(arr) % 2 != 0:
        middle = len(arr) // 2
        if arr[0] != arr[middle]:
            arr[0] = arr[middle]
            return 1

    # The first and last elements are odd
    if len(arr) % 2 == 0:
        middle = len(arr) // 2 - 1
        if arr[0] != arr[middle + 1] or arr[middle] != arr[-1]:
            arr[0] = arr[middle + 1]
            arr[middle] = arr[-1]
            return 2

    # The first, last, and middle elements are odd
    if len(arr) % 2 == 0:
        middle = len(arr) // 2
        if arr[0] != arr[middle + 1] or arr[middle] != arr[-1]:
            arr[0] = arr[middle + 1]
            arr[middle] = arr[-1]
            return 2

    # The first element is odd
    if len(arr) % 2 != 0:
        middle = len(arr) // 2
        if arr[0] != arr[middle]:
            arr[0] = arr[middle]
            return 1

    # Now check the middle
    middle = len(arr) // 2
    if arr[middle] != arr[-1 - middle]:
        arr[middle] = arr[-1 - middle]
        return 1

    return 0
