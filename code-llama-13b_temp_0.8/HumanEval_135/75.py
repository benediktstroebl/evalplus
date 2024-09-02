
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr or len(arr) == 1:
        return -1

    # Declare variables for later use
    largest_index = None
    element_to_left = None

    for index, element in enumerate(arr):
        # Skip the first element because it has no element to the left of it
        if index == 0:
            continue

        # If this is the largest element so far, save it
        if element > element_to_left:
            largest_index = index
            element_to_left = element

    # The largest index will be None if there are no elements greater than the
    # first
    return largest_index
