
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for idx, val in enumerate(arr):
        if idx == 0:
            previous = val
            continue
        first = val
        second = arr[idx - 1]
        if first < second:
            return idx - 1
        previous = val

    return -1

assert can_arrange([1,2,4,3,5]) == 3
assert can_arrange([1,2,3]) == -1
assert can_arrange([5,2,1]) == 0
assert can_arrange([5,3,1,2]) == 2
assert can_arrange([5,4,1,2]) == -1
assert can_arrange([5,3,1,4]) == 2
assert can_arrange([]) == -1
assert can_arrange([1]) == 0
assert can_arrange([2,1]) == 1
