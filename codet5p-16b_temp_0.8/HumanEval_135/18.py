
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for k,v in d.items():
        if v == 1:
            return arr.index(k)
    return -1
