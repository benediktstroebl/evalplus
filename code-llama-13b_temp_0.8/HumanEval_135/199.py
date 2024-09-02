
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # loop through the array
    # check if the element at the current index is not greater than
    # the element at the previous index
    # if the condition is false, return the current index
    # else return -1
    for i in range(len(arr) - 1):
        if not arr[i] <= arr[i + 1]:
            return i
    return -1

