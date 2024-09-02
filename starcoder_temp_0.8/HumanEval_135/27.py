
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Get the length of the array
    n = len(arr)

    # Loop over the elements of the array
    for i in range(1, n):
        # If the element is less than or equal to the element immediately
        # preceding it, then return -1
        if arr[i] <= arr[i - 1]:
            return -1

    # Return the last index
    return n - 1
