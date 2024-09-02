
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_val = 0
    max_ind = -1

    for ind, val in enumerate(arr):
        if val >= max_val:
            max_ind = ind
            max_val = val

    return max_ind
