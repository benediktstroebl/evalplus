
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
    def compare_arr(arr, index):
        # if index == arr_len - 1:
        #     return -1
        if arr[index] <= arr[index + 1]:
            return index
        else:
            return compare_arr(arr, index + 1)
    return compare_arr(arr, 0)

