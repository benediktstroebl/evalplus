
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # write your code here
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return -1
        else:
            return 0
    index = 1
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return index
    return index
