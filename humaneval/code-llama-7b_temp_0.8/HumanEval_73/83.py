
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
    new_arr = sorted(arr)
    l = len(arr)
    s = 0
    i = l - 1
    while i >= l // 2:
        if arr[i] != new_arr[i]:
            s += 1
        i -= 1
    if s % 2 == 0:
        return s // 2
    else:
        return s // 2 + 1

