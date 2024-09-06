
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
    if len(arr) == 1:
        return 0

    min_value = min(arr)
    for index, value in enumerate(arr):
        if index > 0 and value < arr[index - 1]:
            return index - 1

    return -1

