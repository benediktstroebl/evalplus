
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # when there's one or less elements in the list, the largest index is -1
    if len(arr) <= 1:
        return -1

    # initialize the index for the largest index to 1
    # if the largest index is 0, there's nothing to arrange
    index = 1

    # loop through the list, starting at index 1
    # if the element is greater than or equal to the element preceding it
    # then set the largest index to the current index
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            index = i

    # if the largest index is the last index, return -1
    if index == len(arr) - 1:
        return -1

    return index

