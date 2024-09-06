
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    prev = lambda t: t-1 if t > 0 else -1
    for i in range(len(arr)):
        val = arr[i]
        if val > prev(val):
            continue
        else:
            return i
    return -1

