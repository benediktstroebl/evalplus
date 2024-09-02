
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    last_index = 0
    for index, item in enumerate(arr):
        if item <= arr[index - 1]:
            last_index = index - 1
        if item == arr[index - 1]:
            continue
        if item < arr[index - 1]:
            return last_index
    return -1

