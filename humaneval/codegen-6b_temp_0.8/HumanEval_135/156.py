
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) <= 2:
        return -1

    min_el = min(arr)
    max_el = max(arr)

    f = {}
    for i in range(min_el, max_el + 1):
        f[i] = -1

    for el in arr:
        if el in f:
            return f[el]
        min_el = min(min_el, el)
        max_el = max(max_el, el)

    return -1

