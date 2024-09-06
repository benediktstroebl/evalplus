
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
    arr = sorted(arr)
    half_len = len(arr) // 2
    if len(arr) % 2 == 0:
        return min(arr[half_len-1] - arr[half_len], arr[half_len] - arr[half_len-1])
    else:
        return arr[half_len] - arr[half_len-1]

assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 3, 2]) == 1
assert smallest_change([2, 2, 2, 2]) == 0
assert smallest_change([]) == 0
assert smallest_change([1]) == 0
assert smallest_change([1, 2]) == 1
assert smallest_change([1, 2, 3]) == 2
assert smallest_change([1, 2, 3, 4]) == 3
assert smallest_change([1, -2, 3, 4, -3]) == 3
