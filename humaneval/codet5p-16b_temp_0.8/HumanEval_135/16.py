
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    n = arr.index(max(arr))
    if n == 0:
        return -1
    while n > 0:
        if arr[n-1] < arr[n]:
            return n
        n -= 1
    return -1

