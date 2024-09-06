
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    def can_arrange(arr):
        arr_index = []
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr_index.append(i)
        return arr_index[-1] if arr_index else -1
    return can_arrange(arr)
