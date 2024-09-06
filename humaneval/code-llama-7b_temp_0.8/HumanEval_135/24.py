
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    result = -1

    # Track the last element we've seen, and the first index we've seen it at.
    last_element = -1
    last_element_first_index = -1

    # The first index we've seen it at.
    current_index = 0

    for element in arr:
        if element < last_element:
            # We've hit a bad spot.
            return -1

        if element > last_element:
            # We've hit a good spot.
            result = current_index

        last_element = element
        last_element_first_index = current_index

        current_index += 1

    return result
