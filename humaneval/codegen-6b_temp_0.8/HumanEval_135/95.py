
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Work out the longest increasing sequence
    lis = 1
    lis_end = -1
    while lis_end < len(arr) - 1:
        lis_end = lis
        lis += 1
        for i in range(lis, len(arr)):
            if arr[i] >= arr[i - lis]:
                lis += 1
                lis_end = i
                break
    # Now search for the first element
    for i in range(lis, len(arr)):
        if arr[i] <= arr[lis_end - 1]:
            return i
    return -1
