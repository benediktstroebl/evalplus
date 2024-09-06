
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    left = []
    right = []
    for x in arr:
        if not left or left[-1] <= x:
            left.append(x)
        else:
            right.append(x)

    for x in reversed(right):
        if not left or left[-1] <= x:
            left.append(x)
        else:
            return -1

    return len(left) - 1

