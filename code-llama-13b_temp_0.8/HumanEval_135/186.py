
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    i = 0
    prev = None
    while i < len(arr):
        if prev is None or prev <= arr[i]:
            prev = arr[i]
            i += 1
        else:
            break
    if i >= len(arr):
        return -1
    return i - 1

