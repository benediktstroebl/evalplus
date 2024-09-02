
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Find the index of the smallest element which is greater than the element
    # immediately before it
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            minimum_index = i
    # If no such element exists return -1
    if minimum_index == 0:
        return -1
    # Otherwise return the index of the smallest element greater than the
    # element immediately before it
    return minimum_index - 1

