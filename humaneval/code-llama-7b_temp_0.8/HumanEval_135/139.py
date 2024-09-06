
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Avoid index error
    if len(arr) == 1:
        return -1

    # Find out which indices are the largest
    largest_idx = []
    largest_val = max(arr)
    for idx, val in enumerate(arr):
        if val == largest_val:
            largest_idx.append(idx)

    # If no largest values exist
    if len(largest_idx) == 0:
        return -1

    # Iterate through the array backwards from the largest value to find the
    # largest index not greater than or equal to the element preceding it
    index = largest_idx[0]
    for idx in range(index - 1, -1, -1):
        if arr[idx] <= arr[idx + 1]:
            return index

    # If the largest value is the first value in the array then return -1
    return -1

