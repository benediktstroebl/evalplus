
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    for index, value in enumerate(arr):
        # If the value is greater than or equal to the value of the previous index,
        # it cannot be arranged.
        if value >= arr[index - 1]:
            return -1

    return index

