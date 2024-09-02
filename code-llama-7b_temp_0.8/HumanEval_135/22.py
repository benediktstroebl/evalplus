
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # First we will find the largest value in the array.
    # We will then look for the first index in the array where the
    # value is less than or equal to the largest value. If the index
    # exists return that index.
    # If no such index exists we will return -1.
    #
    # Time: O(n)
    # Space: O(1)
    if not arr:
        return -1
    largest_val = -1
    for val in arr:
        if val > largest_val:
            largest_val = val

    found_index = -1
    for index, val in enumerate(arr):
        if val <= largest_val and index > found_index:
            found_index = index

    return found_index

