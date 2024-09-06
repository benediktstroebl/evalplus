
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # 0. Set -1 as result
    result = -1
    # 1. Check that all elements are integers
    if any(not isinstance(el, int) for el in arr):
        return result
    # 2. Check that there are at least 2 elements
    if len(arr) < 2:
        return result
    # 3. Return result
    return result
