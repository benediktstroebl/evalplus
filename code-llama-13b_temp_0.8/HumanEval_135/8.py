
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return 1
        else:
            return 0

    if arr[0] < arr[1]:
        i = 1
    else:
        i = 0
        while i < len(arr) - 1:
            if arr[i] < arr[i + 1]:
                break
            i += 1
    return i

