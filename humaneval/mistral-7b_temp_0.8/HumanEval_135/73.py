
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # return index of element which is not greater than or equal to the
    # element immediately preceding it



    if len(arr) < 2:
        return -1

    # start with the last element
    i = len(arr) - 1

    while arr[i] <= arr[i - 1]:
        if i == 0:
            return -1
        i -= 1
    return i

