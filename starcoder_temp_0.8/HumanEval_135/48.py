
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for idx in range(len(arr)-1, -1, -1):
        if idx == 0:
            return arr[idx]
        elif arr[idx] >= arr[idx-1]:
            return idx-1
    return -1
