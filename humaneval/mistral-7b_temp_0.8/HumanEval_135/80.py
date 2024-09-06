
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_len = len(arr)
    if arr_len < 2:
        return -1

    smallest_element = arr[0]
    smallest_index = 0

    for i in range(1, arr_len):
        if arr[i] > smallest_element:
            return smallest_index
        smallest_element = arr[i]
        smallest_index = i

    return smallest_index
