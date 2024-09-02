
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Could also use an index for current and next values and
    # return the index of the first item that is smaller
    # than the previous item.

    # Can also use a dictionary to check if an item has already been seen
    # and return the index of the first item that is smaller than the
    # previous item

    # Can also use a set to check if an item has already been seen
    # and return the index of the first item that is smaller than the
    # previous item
    seen = set()
    for i, e in enumerate(arr):
        if e not in seen:
            seen.add(e)
        else:
            return i
    return -1

