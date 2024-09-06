
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    d = {arr[-1]: 0}
    for i in range(1, len(arr)):
        if temp := arr[i] - arr[i - 1] - 1:
            d[temp] = temp
        else:
            d[temp + 1] = temp + 1
    return max(d, key=d.get) if d else -1

