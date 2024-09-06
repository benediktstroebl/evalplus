
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # check if the array has duplicates
    if arr.count(arr[0]) > 1:
        raise ValueError("The array has duplicate elements")

    # initialize variables to control the search
    previous = arr[0] - 1
    current = 0
    largest = -1

    # loop over the array
    while current < len(arr):
        if arr[current] <= previous:
            largest = max(largest, current)
        previous = arr[current]
        current += 1

    return largest

