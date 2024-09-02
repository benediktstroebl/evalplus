
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    i = 0
    j = len(arr) - 1
    while i < len(arr) and j >= 0:
        if arr[j] > arr[i]:
            j = j - 1
        elif arr[j] <= arr[i]:
            arr[j] = -1
            i = i + 1
            j = len(arr) - 1
    if -1 in arr:
        return arr.index(-1)
    else:
        return -1

