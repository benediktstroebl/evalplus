
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Initialize result
    res = -1

    # Iterate through array
    for i in range(len(arr)):
        if arr[i] >= arr[i - 1]:
            # Compare element to element in front of it
            if arr[i] < arr[res]:
                # If element to the left is greater than the element to the right
                # Update result
                res = i
    return res

