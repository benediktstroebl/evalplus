
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    maxes = {}
    for i in range(len(arr)):
        if arr[i] in maxes:
            maxes[arr[i]] = 0
        if arr[i-1] not in maxes:
            maxes[arr[i-1]] = i-1
        else:
            maxes[arr[i]] = max(maxes[arr[i-1]], i-1)
    return max(maxes.values())

