
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1

    if len(arr) == 1:
        return 0

    for i in range(0, len(arr) - 1):
        j = i
        while arr[j] >= arr[j + 1]:
            j += 1

        if arr[i] >= arr[j]:
            return -1

    return j

