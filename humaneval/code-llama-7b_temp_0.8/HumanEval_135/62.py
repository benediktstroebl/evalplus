
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    min_value = min(arr)
    max_value = max(arr)
    for i in range(min_value, max_value+1):
        if arr[i-1] <= i:
            return i-1
    return -1

