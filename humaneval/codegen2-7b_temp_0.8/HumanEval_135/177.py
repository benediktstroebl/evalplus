
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    l = []
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            l.append(i)
    if l == []:
        return -1
    else:
        return l[-1]
