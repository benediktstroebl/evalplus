
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
    changes = 0
    for i in range(len(arr)):
        if arr[i] != arr[-i-1]:
            changes += 1
    return changes


assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([2,1,3]) == 1
assert smallest_change([1,2,3,2,1]) == 1
assert smallest_change([1,2,3,2,1,4]) == 2
assert smallest_change([1,2,3,2,1,2,3]) == 3
assert smallest_change([1,2,3,2,1,2,3,3]) == 4
assert smallest_change([1,2,3,2,1,2,3,3,4]) == 5
assert smallest_change([1,2,3,2,1,2,3,3,4,4,3,2]) == 6
assert smallest_change([2,1,3]) == 1
assert smallest_change([1,2,3,2,1]) == 0
assert smallest_change([1,2,3,2,1,4]) == 2
assert smallest_change([1,2,3,2,1,2,3]) == 3
assert smallest_change([1,2,3,2,1,2,3,3]) == 4
assert smallest_change([1,2,3,2,1,2,3,3,4]) == 5
assert smallest_change([1,2,3,2,1,2,3,3,4,4,3,2]) == 6
assert smallest_change([2,1,3]) == 1
assert smallest_change([1,2,3,2,1]) == 0
assert smallest_change([1,2,3,2,1,4]) == 2
assert smallest_change([1,2,3,2,1,2,3]) == 3
assert smallest_change([1,2,3,2,1,2,3,3