
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

    count = 0
    # find first index where array is not palindromic
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            break
    else:  # if for loop finished normally, the array is palindromic
        return 0

    # loop over half of the array to find the first index where the value can be changed to be the same as the mirror
    for j in range(i, len(arr) - i):
        # find the first value that is the same as the mirror
        if arr[j] == arr[len(arr) - j - 1]:
            count += 1
            break

    return len(arr) - count - 2 * i
