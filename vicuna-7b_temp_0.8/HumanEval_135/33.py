
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    i = 0
    while i < n-1:
        j = i + 1
        while j < n and arr[i] <= arr[j]:
            j += 1
        if j - i == 1:
            return i
        i = j
    return -1