
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # For each element in the array, we need to check that it is not greater
    # than or equal to the element immediately preceding it. If it is, then
    # the element at the current index is the largest element which is not
    # greater than or equal to the element immediately preceding it.
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return i

    # If we reached this point, then the last element is the largest element
    # which is not greater than or equal to the element immediately preceding
    # it.
    return len(arr) - 1

