
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    sorted_arr = sorted(arr)
    result = -1
    for i in range(len(sorted_arr)):
        if i == 0 or sorted_arr[i] > sorted_arr[i-1]:
            result = i
        else:
            break
    return result
