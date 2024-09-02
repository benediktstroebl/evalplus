
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

    # https://www.geeksforgeeks.org/minimum-number-changes-required-make-an-array-palindromic/
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0 if arr[0] == 1 else 1
    odd = 0
    for i in arr:
        if i % 2 == 0:
            continue
        else:
            odd += 1
    return len(arr) - odd + 1 if odd == 0 else len(arr) - odd
