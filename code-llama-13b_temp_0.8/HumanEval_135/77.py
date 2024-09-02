
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    visited = set()
    for i, v in enumerate(arr):
        if v in visited:
            continue
        remaining = set(arr) - visited
        if v - 1 in remaining:
            return i
        if v + 1 in remaining:
            return i + 1
        visited.add(v)
    return -1
