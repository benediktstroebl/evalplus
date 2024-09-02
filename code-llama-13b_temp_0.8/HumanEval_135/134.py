
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Checks for duplicate values in arr
    arr_set = set(arr)
    if len(arr_set) < len(arr):
        return -1
    # Sort the array
    arr_sorted = sorted(arr)
    # Iterate through the array. If element > prev_element, return i-1
    prev_elem = arr_sorted[0] - 1
    for i, elem in enumerate(arr_sorted):
        if elem < prev_elem:
            return i - 1
        prev_elem = elem
    # No elem is < prev_elem
    return -1
    

