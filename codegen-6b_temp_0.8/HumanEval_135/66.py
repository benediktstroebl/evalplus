
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def arr_find_lice_by_index(arr, index):
        if index == 0 or arr[index] < arr[index - 1]:
            return index

        return arr_find_lice_by_index(arr, index - 1)

    if not arr:
        return -1

    return arr_find_lice_by_index(arr, len(arr) - 1)

