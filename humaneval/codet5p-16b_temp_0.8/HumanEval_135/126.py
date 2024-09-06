
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    ordered = arr[:]
    ordered.sort()
    index = 0
    while index < len(ordered):
        try:
            if ordered[index] >= ordered[index - 1]:
                index += 1
                continue
            else:
                return index - 1
        except IndexError:
            return -1

    return -1
