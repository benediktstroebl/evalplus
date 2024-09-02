
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
    arr = sorted(arr)
    # Case 1 - the array is already palindromic
    if arr == arr[::-1]:
        return 0

    # Case 2 - number of elements is odd and there is no element that matches the middle element
    if len(arr) % 2 != 0 and len(set(arr)) == len(arr):
        return -1

    # Case 3 - number of elements is even and there is no pair of elements that matches each other
    if len(arr) % 2 == 0 and len(set(arr)) < len(arr):
        return -1

    # Case 4 - number of elements is odd and there is an element that matches the middle element
    if len(arr) % 2 != 0 and len(set(arr)) == len(arr) - 1:
        return 1

    # Case 5 - number of elements is even and there is a pair of elements that matches each other
    if len(arr) % 2 == 0 and len(set(arr)) < len(arr) - 1:
        return 2

