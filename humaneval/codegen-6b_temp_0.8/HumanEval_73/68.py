
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

    if n % 2 == 0:
        return min(n - 1, n // 2)
    else:
        return min(n - 1, n // 2 + 1)

assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1,2,3,1,1]) == 2
assert smallest_change([1,2,3,1,1,3]) == 2
assert smallest_change([1,2,1,2,1]) == 2
assert smallest_change([1,2,1,2,1,1]) == 0
assert smallest_change([1,2,1,2,1,1,1]) == 2
assert smallest_change([1,1,1]) == 0
assert smallest_change([1,2,2,1,2,1,2,1]) == 2
assert smallest_change([1,2,2,1,2,1,2,1,2,1]) == 2
assert smallest_change([28,27,26,25,25,26,26,27,26,27,27,30,23,23,23,23,25,25,26,28,28,30,24,22,22,22,22,22,22,22,22,22,23,23,23,23,22,22,22,22,22,23,23,23,23,22,22,25,25,26,25,27,27,26,27,26,25,26,25,26,28,27,27,27,30,25,25,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23,23,23,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22