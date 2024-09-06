
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    current = arr[0]
    largest_preceding_index = -1

    for index in range(0,len(arr)):
        if arr[index] > current:
            largest_preceding_index = index
            current = arr[index]

    return largest_preceding_index
