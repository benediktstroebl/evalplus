
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) <= 1:
        return -1

    for i in range(len(arr) - 1):
        if arr[i + 1] >= arr[i]:
            continue
        else:
            next_greater = -1
            for j in range(i + 1, len(arr)):
                if arr[j] <= arr[i]:
                    next_greater = j
                    break
            return next_greater

    return -1
