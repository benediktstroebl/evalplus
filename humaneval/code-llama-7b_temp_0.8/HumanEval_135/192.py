
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1

    # i is the index of current element.
    # j is the index of previous element.
    i = 1
    j = 0

    # Find the element of index i which is not greater than or equal to the
    # element at index j.
    while i < len(arr):
        if arr[i] <= arr[j]:
            j = i
            i += 1
        else:
            # Increase i because there are no elements greater than or equal to
            # the previous element.
            i += 1

    # The element at index j is either the maximum element or is greater than
    # all the previous elements.
    return j

