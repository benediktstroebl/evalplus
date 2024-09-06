
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    i = 0
    max_index = -1
    while i < len(arr) - 1:
        # If arr[i] <= arr[i + 1], increment i
        # otherwise set max_index to i and i += 1
        if arr[i] <= arr[i + 1]:
            i += 1
        else:
            max_index = i
            i += 1

    if i == len(arr) - 1:
        return max_index

    return -1

