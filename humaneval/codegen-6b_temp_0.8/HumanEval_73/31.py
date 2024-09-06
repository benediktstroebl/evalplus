
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

    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 1
        else:
            return 0

    # arr is now [1,2,3,4,3,2,2]
    val, min_change = arr[0], -1
    for i in xrange(1, len(arr)):
        new_val = arr[i]
        tmp = val
        val = new_val
        if new_val < tmp:
            min_change = i - 1
        elif new_val > tmp:
            min_change = i - 1

    if min_change == -1:
        return 0
    else:
        return len(arr) - min_change - 1

