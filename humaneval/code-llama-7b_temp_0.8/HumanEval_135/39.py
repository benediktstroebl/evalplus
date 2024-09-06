
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    #if len(arr) < 2: return -1

    # get the maximum element
    # loop through the list and check if it's greater than the max element.
    # If so, update the max element, and the maximum index.
    # Return the max index.

    max_elem = max(arr)
    max_index = -1

    for i in range(len(arr) - 1):
        if arr[i + 1] >= arr[i]:
            if arr[i + 1] == max_elem:
                max_index = i + 1
            if arr[i + 1] > max_elem:
                max_elem = arr[i + 1]
                max_index = i + 1

    return max_index
