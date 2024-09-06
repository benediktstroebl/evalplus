
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # get the max and min values
    max_v, min_v = max(arr), min(arr)
    # return the index of the first number larger than min_v that is less
    # than max_v
    for idx, v in enumerate(arr):
        if v > min_v and v < max_v:
            return idx
    # otherwise, return -1
    return -1
