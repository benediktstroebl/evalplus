
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check if the first element is greater than or equal to the second element
    if arr[0] >= arr[1]:
        return -1
    
    # Initialize the largest index to the first element
    i = 0
    
    # Iterate through the array
    for j in range(1, len(arr)):
        if arr[j] > arr[i]:
            i = j
    
    return i