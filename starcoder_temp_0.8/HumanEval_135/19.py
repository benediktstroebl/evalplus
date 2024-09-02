
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    last_num = float("-inf")
    last_ind = -1
    for i, num in enumerate(arr):
        if num >= last_num:
            last_num = num
            last_ind = i
    return last_ind

