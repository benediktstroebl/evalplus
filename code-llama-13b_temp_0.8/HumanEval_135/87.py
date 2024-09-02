
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # def _rev(v):
    #     return -v
    # index = len(arr) - 1
    # sorted_arr = sorted(arr, key=_rev)
    # while index >= 0:
    #     if sorted_arr[index] < sorted_arr[index + 1]:
    #         return index
    #     index -= 1
    # return -1

    # index = len(arr) - 1
    # # sorted_arr = sorted(arr)
    # while index >= 0:
    #     if arr[index] < arr[index - 1]:
    #         return index
    #     index -= 1
    # return -1

    index = len(arr) - 1
    sorted_arr = sorted(arr)
    while index >= 0:
        if sorted_arr[index] < sorted_arr[index - 1]:
            return index
        index -= 1
    return -1
