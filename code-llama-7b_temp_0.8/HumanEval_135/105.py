
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) <= 1:
        return -1
    i, j = 0, 1
    while j < len(arr):
        if arr[j] > arr[i]:
            i += 1
        elif arr[j] < arr[i]:
            j += 1
        else:
            return -1
    return i

