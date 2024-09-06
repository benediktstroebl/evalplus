
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check for duplicate values
    seen = set()
    i = 0
    while i < len(arr) - 1:
        if arr[i] in seen:
            return -1
        seen.add(arr[i])
        i += 1
    return i+1
