
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # start with the end of the list and work back towards the beginning
    # if at any point we find a number greater than or equal to the one
    # before it, then return the index of the number that is greater
    # if we never find such a number, then return -1

    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= arr[i-1]:
            return i
    return -1

