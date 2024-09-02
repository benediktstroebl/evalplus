
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr.sort()
    # Get the list of differences
    diffs = list(map(lambda x, y: y - x, [0] + arr[:-1], arr))

    # Look at the list of differences in reverse order
    for i, diff in enumerate(diffs[::-1]):
        if diff == 1:
            return len(arr) - 1 - i
        elif diff == 2:
            return len(arr) - 2 - i
    return -1
