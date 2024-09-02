
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    x = 0
    y = 1
    while y < len(arr):
        if arr[y] > arr[x]:
            return y
        x = y
        y += 1
    return -1
