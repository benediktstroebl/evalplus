
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # sort array
    arr.sort()

    # check if any element in array is greater than its previous one
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            return -1

    # if all elements in array are non-decreasing, then the
    # largest index of an element which is not greater than or equal
    # to the element immediately preceding it is the last element in the array
    return len(arr) - 1

