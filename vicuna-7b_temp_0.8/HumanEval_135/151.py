
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check if the input array is not empty
    if len(arr) == 0:
        return -1

    # Check if the input array is a sorted array
    if not sorted(arr):
        return -1

    # Create a dictionary to store the indices of the elements
    indices = {}

    # Iterate through the array
    for i, val in enumerate(arr):
        # If the element is not in the dictionary, add it and its index
        if val not in indices:
            indices[val] = i

    # Return the largest index of an element which is not greater than or equal
    # to the element immediately preceding it
    return max(indices, key=indices.get)