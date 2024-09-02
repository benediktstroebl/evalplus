
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Validate input
    if not arr:
        return -1

    # Set up variables
    largest_value = max(arr)
    largest_index = largest_value - 1

    # Loop through array
    for i in range(len(arr)):
        if arr[i] <= arr[largest_index]:
            largest_index = i
        elif i > largest_index:
            largest_index = -1
            break

    return largest_index
