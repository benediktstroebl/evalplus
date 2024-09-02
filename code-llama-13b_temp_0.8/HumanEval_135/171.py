
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    min_value = arr[0]
    for i, value in enumerate(arr):
        if value < min_value:
            return i - 1
        min_value = min(min_value, value)
    return -1

