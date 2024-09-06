
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    largest = len(arr) - 1
    current = 0
    while current < largest:
        if arr[current] <= arr[current + 1]:
            current += 1
        else:
            largest = current
    if largest == 0:
        return -1
    return largest
