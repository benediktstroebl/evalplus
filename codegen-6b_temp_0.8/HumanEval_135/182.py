
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    result = -1
    for i, a in enumerate(arr):
        j = a - 1
        while j >= 0 and arr[j] > a:
            j -= 1
        if j >= 0:
            result = max(result, i - j)
    return result

