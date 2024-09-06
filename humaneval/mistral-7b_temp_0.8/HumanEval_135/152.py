
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # first, create an index (x) that holds the value of the index
    # we are currently looking at
    x = 0
    # now, we want to look for a value (y) that is less than the current value
    # but which is larger than all the values that come before it
    # if we can't find such a value, return -1
    while x < len(arr):
        if arr[x] > arr[x+1] and arr[x] > arr[y] for y in range(x):
            return x
        else:
            x += 1
            y += 1
    return -1
