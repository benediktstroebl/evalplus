
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    seen = {x: False for x in arr}
    i = 0
    while i < len(arr):
        if seen[arr[i]] == False:
            seen[arr[i]] = True
            i += 1
        else:
            return i - 1
    return -1

