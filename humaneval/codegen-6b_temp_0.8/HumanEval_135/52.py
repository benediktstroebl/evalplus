
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for i, value in enumerate(arr):
        next_value = arr[i + 1] if i < (len(arr) - 1) else None
        if next_value is not None and next_value > value:
            return i

    return -1

