
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    current = 0
    max_index = 0
    while current < len(arr) - 1:
        if arr[current] <= arr[current + 1]:
            current += 1
        else:
            max_index = max(current, max_index)
            current += 2
    return max_index


