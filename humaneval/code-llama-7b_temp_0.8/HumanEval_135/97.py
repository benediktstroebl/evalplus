
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # create a list with the same length as the given array, each
    # element initialized to the smallest value in the array
    # we will update each element to the index of the smallest
    # value that is not greater than or equal to the previous value
    # or -1 if there are no such values
    arr_size = len(arr)
    prev = [0] * arr_size
    for i in range(arr_size):
        prev[i] = min(arr[i:])
    for i in range(arr_size):
        if prev[i] == arr[i]:
            prev[i] = -1
    print("prev: ", prev)

    # look for the last index which has not been updated
    index = arr_size - 1
    while index > -1:
        if prev[index] == -1:
            break
        index -= 1

    return index

