
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr = [abs(i - val) for i, val in enumerate(arr)]
    min_arr = [a for a in arr if a == min(arr)]
    if min_arr:
        return arr.index(min(min_arr))

    return -1

