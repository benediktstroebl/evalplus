
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
    i = 0
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            break
        i += 1
    if i == len(arr):
        return -1
    else:
        return i - 1

