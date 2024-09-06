
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Remove duplicates from the array.
    uniq_arr = list(set(arr))
    for i in range(len(uniq_arr)):
        if i == 0:
            if uniq_arr[i] - 1 >= uniq_arr[i+1]:
                return i
        elif i == len(uniq_arr) - 1:
            if uniq_arr[i] - 1 >= uniq_arr[i-1]:
                return i
        elif uniq_arr[i] - 1 >= uniq_arr[i-1] and uniq_arr[i] - 1 >= uniq_arr[i+1]:
            return i

    return -1

