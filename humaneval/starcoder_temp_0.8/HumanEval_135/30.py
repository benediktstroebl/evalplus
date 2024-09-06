
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    seen = {}
    for i, num in enumerate(arr):
        if num not in seen:
            seen[num] = i
        else:
            return seen[num]
    return -1
