
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    #
    #  First of all, sort the array.
    #
    arr.sort()

    #
    #  Now, scan the array. If the current element is greater than or equal
    #  to the previous one, we're done. If the current element is less than
    #  the previous, return the index of the previous element.
    #
    prev = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            return -1

        if arr[i] < arr[i - 1]:
            return i - 1

    return -1
