
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    maximum = 0
    for index, element in enumerate(arr):
        if index > 0:
            if element <= arr[index-1]:
                maximum = index - 1
                break
    # if maximum in range(0, len(arr)):
    return maximum
    # return -1 if maximum not in range(0, len(arr)) else maximum

