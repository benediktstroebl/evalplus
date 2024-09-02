
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
    if len(arr) <= 2:
        return 0

    sum_before = 0
    sum_after = 0
    for i in range(len(arr) // 2):
        sum_before += arr[i]
        sum_after += arr[~i]

    return abs(sum_before - sum_after)

