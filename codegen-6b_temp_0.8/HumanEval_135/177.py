
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Brute force, checking for largest index of element which is not
    # less than the element immediately before it.
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] >= arr[i]:
                break
        else:
            return i
    return -1

