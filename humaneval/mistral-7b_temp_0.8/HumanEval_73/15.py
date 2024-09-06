
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
    if arr == []:
        return []
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return abs(arr[0] - arr[1])
    # first case: all of the array is palindromic
    if arr[0] == arr[-1]:
        return 0

    # all cases except the above
    min_diff = abs(arr[0] - arr[-1])
    i = 1
    while i < len(arr):
        if arr[i] == arr[i - 1]:
            i += 1
            continue
        # here the case when arr[i] is not equal to arr[i - 1]
        if arr[i] == arr[-1]:
            # so we can make arr[i - 1] to arr[i] and we can make arr[-1] to arr[i]
            diff = abs(arr[i - 1] - arr[-1])
            # we take the minimum between diff and min_diff
            min_diff = min(diff, min
