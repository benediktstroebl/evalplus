
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
    if not arr:
        return 0

    arr_len = len(arr)
    mini = 1
    for i in xrange(arr_len):
        for j in xrange(arr_len-i):
            if arr[j] != arr[j+i]:
                mini = min(mini, arr_len - j - i)
    return mini

