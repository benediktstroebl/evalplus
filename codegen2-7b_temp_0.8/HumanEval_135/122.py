
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max = arr[0]
    if arr[0] <= arr[1]:
        max = arr[1]
    for i in range(1, len(arr) - 1):
        if arr[i] >= max:
            max = arr[i]
    if max <= arr[len(arr) - 2]:
        return max
    return -1
