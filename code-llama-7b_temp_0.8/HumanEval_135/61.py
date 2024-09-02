
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_copy = arr[:]
    arr_copy.sort()
    for i in range(len(arr)):
        if arr_copy[i] <= arr[i]:
            continue
        elif i < len(arr) - 1 and arr_copy[i] <= arr[i+1]:
            return i
        elif i == len(arr) - 1 and arr_copy[i] <= arr[i]:
            return i
    return -1

