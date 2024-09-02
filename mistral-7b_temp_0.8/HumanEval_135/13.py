
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Write your code here
    # Initialise result
    result = -1

    # Traverse the array from the last element
    for i in range(len(arr)-1, -1, -1):
        # If the current element is greater than the element immediately
        # preceding it, update the result
        if arr[i] > arr[i-1]:
            result = i
        # If the current element is less than or equal to the element
        # immediately preceding it, break
        else:
            break
    return result


