
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ### No need to sort -- O(n log n)
    ### Check if the value at index i is less than or equal to the
    ### element at index i-1. If so, return i. If i == 0, return -1
    ### since there is no index i-1 for it. If i == len(arr), return -1
    ### because there is no element at index i+1 for it.
    ### O(n) time and O(1) space.
    i = 0
    while i < len(arr):
        if i > 0 and arr[i] <= arr[i - 1]:
            return i
        if i == len(arr) - 1:
            return -1
        i += 1
    return -1

