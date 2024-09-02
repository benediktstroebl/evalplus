
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not isinstance(arr, list) or len(arr) == 0:
        return -1

    previous = None
    for i in range(len(arr)):
        if arr[i] == previous:
            continue
        if arr[i] > previous:
            return i
        previous = arr[i]
    return -
