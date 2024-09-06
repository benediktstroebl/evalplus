
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # iterate through the array, checking if the current value is less than the previous value.
    for i in range(1, len(arr)):
        # if the current value is less than the previous value, return the index of the current value.
        if arr[i] < arr[i - 1]:
            return i

    # if the loop finishes without returning a value, then there are no elements that are less than the previous element,
    # so return -1.
    return -1

