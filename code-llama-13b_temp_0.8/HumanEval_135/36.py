
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_value = -1
    for idx, val in enumerate(arr):
        if idx == 0:
            max_value = val
        else:
            if val < max_value:
                return idx - 1
            else:
                max_value = val
    return -1

