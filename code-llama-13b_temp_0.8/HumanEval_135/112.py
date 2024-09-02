
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # check for duplicates
    if len(arr) != len(set(arr)):
        return -1
    # use enumerate to get values and indices
    for idx, val in enumerate(arr[:-1]):
        if val >= arr[idx + 1]:
            return idx
    # no match found
    return -1
