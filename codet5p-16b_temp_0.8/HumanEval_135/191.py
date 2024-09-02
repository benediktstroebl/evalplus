
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    pre_num = None

    for i, num in enumerate(arr):
        if num >= pre_num:
            pre_num = num
        else:
            return i - 1

    return -1

