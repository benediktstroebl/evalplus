
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    return_value = 0
    for index, value in enumerate(arr):
        if index > return_value:
            if all(value >= arr[i] for i in range(index)):
                return_value = index
    return return_value

