
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def arr_index(x):
        if x == arr[0]:
            return 0
        if x == arr[-1]:
            return len(arr) - 1
        for index in range(len(arr) - 1):
            if arr[index] <= x < arr[index + 1]:
                return index + 1
        return -1
    return arr_index

