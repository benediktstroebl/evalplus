
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    prev_elem = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1] and arr[i] < prev_elem:
            prev_elem = arr[i]
        else:
            prev_elem = arr[i]
    return -1 if prev_elem == len(arr) - 1 else prev_elem + 1

