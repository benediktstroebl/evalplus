
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # check if empty array
    if not arr:
        return -1

    # sort the array
    arr.sort()

    # check the first element
    if arr[0] < arr[1]:
        return 0

    # check each element
    for i in range(len(arr)):
        if arr[i] > arr[i + 1]:
            return i

    return -1
