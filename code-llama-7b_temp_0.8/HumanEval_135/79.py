
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    #
    # Useful math:
    #
    # E = sum(1/i)
    # E - 1 = sum(1/i - 1)
    # (E - 1)/E = sum((1/i - 1)/i)
    #
    if not arr:
        return -1
    n = len(arr)
    expected = sum(1/i for i in arr)
    actual = (expected - 1)/expected
    return int(round(actual*n)) if actual > 0 else -1
