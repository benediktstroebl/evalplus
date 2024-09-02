
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # If array is empty or only contains one element, then return -1
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return 0

    # Initialize result index
    result = 0
    for i, num in enumerate(arr):
        # if result == -1, then num never occurs before
        if result == -1:
            result = i
        # If result occurs after num, then num cannot occur before result
        elif result < num:
            return -1

    return result

