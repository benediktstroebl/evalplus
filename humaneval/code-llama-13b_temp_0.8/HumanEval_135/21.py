
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # best solution: O(n)
    d = {}
    for idx, elem in enumerate(arr):
        if idx in d:
            del d[idx]
        elif elem in d:
            return d[elem]
        d[elem] = idx
    return -1

