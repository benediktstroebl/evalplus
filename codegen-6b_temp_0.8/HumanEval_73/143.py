
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
    arr.sort()
    change = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[len(arr) - 1 - i]:
            change += 1
        i += 1
    return change


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 4
assert smallest_change([1, 2, 3, 2, 1, 2]) == 2
assert smallest_change([-1, 1, 2]) == 2
assert smallest_change([1, 1, 1, 1]) == 0
assert smallest_change([1, 2, 3]) == 3
assert smallest_change([3, 3, 2, 1, 1]) == 3
assert smallest_change([-1, -1, -1]) == 0
assert smallest_change([3, 2, 1, 1]) == 2
assert smallest_change([1, 3, 2, 1]) == 1
assert smallest_change([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert smallest_change([1, 1, 1, 1, 2, 1, 1, 1]) == 2
assert smallest_change([1, 1, 1, 1, 2, 1, 1, 1, 2]) == 2
assert smallest_change([1, 1, 1, 1, 2, 1, 1, 1, 2, 2]) == 0
assert smallest_change([1, 2, 1, 2, 3, 2, 1, 2, 4, 2, 1, 2, 3, 2, 1, 2]) == 1
assert smallest_change([1, 2, 1, 2, 3, 2, 1, 2, 4, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 1
