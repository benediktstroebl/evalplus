
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # valid for all types of numbers
    # space: O(1)
    # time: O(n)
    last = 0
    for idx, el in enumerate(arr):
        if el < last:
            return idx - 1
        last = el
    return -1
