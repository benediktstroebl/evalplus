
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def sub(arr, index):
        if arr[index-1] > arr[index]:
            return index - 1
        else:
            return -1

    arr = sorted(arr)
    for index, element in enumerate(arr):
        arr[index] = sub(arr, index)
    return max(arr)
