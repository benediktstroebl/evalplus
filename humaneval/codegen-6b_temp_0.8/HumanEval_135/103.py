
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr = [-1] + arr
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            arr[i] = i - 1

    return arr[-1]


assert can_arrange([1, 2, 4, 3, 5]) == 3
assert can_arrange([1, 2, 3]) == -1
assert can_arrange([1, 1, 5, 5, 10]) == 3
assert can_arrange([1, 2, 3, 4]) == -1
assert can_arrange([1, 2, 3, 5, 5, 10]) == 4
assert can_arrange([1, 2, 3, 4, 4]) == -1
assert can_arrange([1, 2, 3, 5, 6]) == -1