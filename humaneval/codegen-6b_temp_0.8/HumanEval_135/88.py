
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1

    previous, current = arr[0], arr[1]

    for index in range(2, len(arr)):
        if current <= previous:
            return index - 1

        previous = current
        current = arr[index]

    return -1

