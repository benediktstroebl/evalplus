
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Initialize result.
    largest_index = -1
    curr_index = -1
    curr_num = 0
    next_num = 0

    # Traverse the array from front to back.
    for i in range(0, len(arr)):
        curr_index = i
        curr_num = arr[i]

        # Check for the next number
        if i+1 < len(arr):
            next_num = arr[i+1]

        # Update the largest index.
        if (curr_num >= next_num):
            largest_index = curr_index

    # Return the result.
    return largest_index
