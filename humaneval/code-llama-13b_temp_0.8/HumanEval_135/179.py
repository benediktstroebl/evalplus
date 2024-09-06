
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # check to see if first element is greater than second
    if arr[0] > arr[1]:
        return 0
    # create array of next largest index of element in arr
    next_largest_index = [0] * len(arr)
    # set 2nd index as next largest index of 2nd element
    next_largest_index[1] = 1
    # set next largest index for all remaining elements
    for i in range(2, len(arr)):
        # check if current element is larger than next element
        if arr[i] > arr[i + 1]:
            # if so, return current index
            return i
        # otherwise, set index of current element as next largest
        next_largest_index[i] = next_largest_index[i + 1]
    # if loop reaches this point, no such element exists
    return -1
