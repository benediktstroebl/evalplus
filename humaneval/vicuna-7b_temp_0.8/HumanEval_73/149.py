
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
    # check if the array is empty or not
    if not arr:
        return 0

    # check if the first and last element are equal or not
    if arr[0] != arr[-1]:
        return 1

    # check if the number of elements that are different from the first element are odd or even
    if (arr[0] != arr[-1]) == len(arr) % 2 == 0:
        return 2
    else:
        return 1

arr = [6, 7, 8, 9, 10, 11, 12]
