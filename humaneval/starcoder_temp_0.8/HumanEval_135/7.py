
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    res = 0
    for idx, val in enumerate(arr):
        if idx > res and val >= arr[res]:
            res = idx
    return res if res < len(arr) else -1
