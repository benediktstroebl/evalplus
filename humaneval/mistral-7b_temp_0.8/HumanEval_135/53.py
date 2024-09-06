
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1
    largest = max(arr)
    if arr[0] < largest:
        return 0
    for i in range(1, len(arr)):
        if arr[i] < largest:
            return i
        largest = max(largest, arr[i])
    return -1

