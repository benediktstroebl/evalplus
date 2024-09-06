
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
    last_index = -1
    while i < len(arr) - 1:
        if arr[i] < arr[i + 1]:
            last_index = i
        i += 1
    return last_index

