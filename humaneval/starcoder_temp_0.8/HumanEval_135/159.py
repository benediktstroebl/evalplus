
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    if len(arr) == 0:
        return -1

    # Iterate through array, checking that each element is less than the
    # element preceding it.
    for idx, item in enumerate(arr):
        if idx > 0:
            if item >= arr[idx - 1]:
                return -1

    # If we're at the end of the array without a mismatch, then return the
    # index of the last item in the array.
    return len(arr) - 1
