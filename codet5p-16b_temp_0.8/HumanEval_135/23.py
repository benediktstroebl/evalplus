
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    smallest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > smallest:
            largest_index = i
            smallest = arr[i]
    if largest_index == 0:
        return -1
    return largest_index
