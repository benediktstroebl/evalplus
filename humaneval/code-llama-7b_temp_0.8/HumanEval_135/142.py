
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # The idea is to use the idea that an element in the input is valid if and
    # only if it is greater than the previous value. This means we only need to
    # look at one value at a time to determine whether or not it's valid, so
    # we can use a loop with a single index to do this.

    # So the first thing we do is to initialize the index to 0. If the array
    # is empty, we return -1.
    index = 0
    if not arr:
        return -1

    # Then we run a loop to check for validity.
    while index < len(arr):
        # If the element at the index is greater than or equal to the element
        # immediately preceding it, then we know the element at the index is
        # invalid, so we return -1.
        if arr[index] >= arr[index - 1]:
            return -1

        # If the element at the index is valid, then we increment the index.
        index += 1

    # If we make it out of the loop without returning -1, then we know all
    # elements are valid. So we return the index, which is the largest index
    # of an element which is not greater than or equal to the element
    # immediately preceding it.
    return index - 1
