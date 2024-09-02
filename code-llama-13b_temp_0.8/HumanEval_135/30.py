
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not len(arr):
        return -1
    maximum = max(arr)
    if maximum * 2 > sum(arr):
        return -1
    # find the minimum index
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= maximum:
            return i

