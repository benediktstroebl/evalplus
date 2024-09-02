
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Sort the array, and look for a pair with a difference greater than 1.
    # Time: O(n*log(n))
    # Space: O(1)
    arr_sorted = sorted(arr)
    for i in range(len(arr) - 1):
        if arr_sorted[i] + 1 < arr_sorted[i + 1]:
            return i
    return -1

