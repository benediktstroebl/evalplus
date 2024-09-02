
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    a = []
    for i in range(len(arr)):
        if arr[i] not in a and i!= 0 and arr[i] >= arr[i - 1]:
            a.append(arr[i])
    if len(a) == 0:
        return -1
    return a[-1
