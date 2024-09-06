
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Sort the array to put in ascending order.
    arr.sort()

    # Start with the second element (first element cannot precede anything).
    for i in range(1, len(arr)):
        # If the current element is less than the element that precedes it.
        if arr[i - 1] > arr[i]:
            # Then the index of the current element is the largest index of an
            # element which is not greater than the element immediately
            # preceding it.
            return i

    # If there are no such elements return -1.
    return -1

