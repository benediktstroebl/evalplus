
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr = sorted(arr)
    end_index = len(arr) - 1
    start_index = 0
    for index in range(1, end_index):
        if arr[index] > arr[index-1]:
            break
        start_index += 1
    return start_index