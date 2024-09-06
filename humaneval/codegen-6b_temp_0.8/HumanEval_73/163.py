
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
    arr.sort()

    # if arr is palindromic break out of the loop
    for i in range(len(arr) // 2):
        if arr[i] != arr[~i]:
            break

    # if we haven't broken out of the loop, return 1
    return 1 if i == len(arr) // 2 else 0

