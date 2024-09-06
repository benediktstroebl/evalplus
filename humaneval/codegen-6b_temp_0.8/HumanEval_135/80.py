
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # With the given array being ordered, the next_greater_element logic
    # will ALWAYS be executed, so we can exclude it from the loop.
    # We can also remove the first element as a check for this edge case.
    # Took a bit of time to figure this out.
    if len(arr) < 2:
        return -1
    elif arr[0] > arr[1]:
        return 0
    # So far, the following logic is executed as long as the first element
    # is greater than the second.
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            return i
    return -1

