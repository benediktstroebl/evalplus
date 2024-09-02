
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

    n = len(arr)
    half_len = n // 2
    changes = 0
    half_arr = arr[:half_len]
    full_arr = arr[half_len:]

    i = 0
    while i < half_len:
        if half_arr[i] != full_arr[i]:
            changes += 1
            half_arr[i] = full_arr[i]
            full_arr[n - 1 - i] = half_arr[i]
        i += 1
    return changes
