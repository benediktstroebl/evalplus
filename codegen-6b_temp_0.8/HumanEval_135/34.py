
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
    index = 0
    while index + 1 < len(arr) and arr[index] < arr[index + 1]:
        index += 1
    return index if index != len(arr) - 1 else -1

