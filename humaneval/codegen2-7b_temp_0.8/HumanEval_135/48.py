
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
    first = arr[0]
    if arr[-1] > first:
        return -1
    for i in range(1,len(arr)):
        if arr[i] >= first and arr[i]!= arr[i-1]:
            return i
    return -1
