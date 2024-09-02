
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    max_num = max(arr)
    max_num_ind = arr.index(max_num)
    if max_num_ind == 0:
        return -1
    else:
        for i in range(max_num_ind):
            if arr[i] < arr[i+1]:
                pass
            else:
                return i
        return -1
