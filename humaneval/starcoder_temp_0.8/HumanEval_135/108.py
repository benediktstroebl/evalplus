
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_len = len(arr)
    if arr_len < 2:
        return -1
    for i, val in enumerate(arr):
        if i == 0:
            prev = val
            continue
        if val < prev:
            return i - 1
        prev = val
    return -1
