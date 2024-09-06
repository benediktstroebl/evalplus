
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    s = sorted(arr)
    idx_max = len(arr)
    for n, i in enumerate(s):
        if n == 0:
            continue
        if i <= s[n - 1]:
            idx_max = n
        else:
            break
    return idx_max

