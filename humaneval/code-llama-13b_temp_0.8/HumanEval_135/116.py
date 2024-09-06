
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Change list to sorted list
    arr = sorted(arr)
    # Index of first item in list
    index = 0
    # Loop through sorted list
    for i in range(len(arr)):
        # Check if value is less than or equal to value in previous index
        if arr[i] <= arr[index]:
            # Add 1 to index
            index += 1
        else:
            # Return index of previous index
            return index
    # Return -1
    return -1
    
