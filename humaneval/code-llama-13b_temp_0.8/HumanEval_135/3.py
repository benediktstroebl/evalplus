
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1
    
    # dictionary to store previous and current index
    # where the key is the previous index and the value is the current index
    prev_index = {}
    for i in range(len(arr)):
        prev_index[i - 1] = i
    
    # starting index
    current_index = len(arr) - 1
    # iterate over the array in reverse
    for i in range(len(arr) - 1, -1, -1):
        if (arr[i] - 1) in prev_index and current_index >= prev_index[arr[i] - 1]:
            # store the current index
            current_index = prev_index[arr[i] - 1] - 1
            # store the previous index
            prev_index[current_index] = i
        elif (arr[i] - 1) not in prev_index:
            return i

    return -1
