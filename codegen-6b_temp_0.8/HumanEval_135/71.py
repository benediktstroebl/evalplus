
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # TODO:
    # Implement the function can_arrange or not.
    # The function must take an array of integers, and return a valid
    # index or -1 (if no such element exists).
    # The index must not be greater than the length of the array.
    #
    # Hint: you might find the sorted() function useful!
    arr = sorted(arr)
    for i, a in enumerate(arr):
        if a > arr[i-1]:
            return i - 1
    return -1

