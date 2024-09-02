
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
    if len(arr) == 1:
        return 0
    for i, _ in enumerate(arr):
        a = arr[i:]
        b = arr[:len(arr) - i]
        if a == a[::-1] and b == b[::-1]:
            return 0
    return 1


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 4, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 3, 2, 5]) == 4
