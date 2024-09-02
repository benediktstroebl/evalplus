
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

    x = arr[-1]

    for i, y in enumerate(arr[:-1]):
        if y > x and y!= arr[i + 1]:
            return i
        elif y == x:
            return -1

    return
