
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    seen = []
    for i in arr:
        if i > seen[-1]:
            seen.append(i)
        elif i < seen[-1]:
            return i
    return -1

