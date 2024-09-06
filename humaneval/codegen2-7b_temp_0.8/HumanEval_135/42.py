
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    l = len(arr)
    if l == 0:
        return -1
    if l == 1:
        return 0
    m = arr[0]
    for i in range(1, l):
        if m <= arr[i]:
            m = arr[i]
    return max(range(l), key=lambda x: arr[x]
