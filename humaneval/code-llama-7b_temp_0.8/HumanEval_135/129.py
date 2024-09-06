
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # if arr is empty return -1
    # if only one value return -1
    # else if value at index is larger than last value then return -1
    # else return last index
    # if the value at index is not larger than last value
    # then get the last index and return last_index - 1
    # else return -1

    if not arr:
        return -1

    last_value = arr[-1]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] <= last_value:
            return i

    return -1

