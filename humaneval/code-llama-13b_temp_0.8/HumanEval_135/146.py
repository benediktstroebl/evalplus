
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Create a sorted copy of the input array
    sorted_arr = sorted(arr)
    # Iterate through the input array and compare each element to the
    # element immediately preceding it
    for i in range(1, len(arr)):
        # If an element in the input array is greater than or equal to the
        # element immediately preceding it, return its index
        if arr[i] >= arr[i - 1]:
            return i
    # If there are no elements in the input array which are greater than or
    # equal to the element immediately preceding it, return -1
    return -1
    
