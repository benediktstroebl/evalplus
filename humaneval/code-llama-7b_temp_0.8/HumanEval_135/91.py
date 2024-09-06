
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check edge cases
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    
    # Set current index
    i = 0
    
    # Loop through array
    while i < len(arr):
        if arr[i] >= arr[i-1]:
            # If index is greater than or equal to previous element, increment
            i += 1
        else:
            # If index is less than previous element, return index of previous
            # element
            return i-1
            
    # If no index exists, return -1
    return -1
