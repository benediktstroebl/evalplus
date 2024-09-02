
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # calculate the indices of the sorted array
    sorted_arr = sorted(arr)
    sorted_index = [0]
    for i in range(1, len(arr)):
        if sorted_arr[i] != sorted_arr[i - 1]:
            sorted_index.append(i)
    # return the first index after a descending sequence
    for i in range(len(sorted_index) - 1, 0, -1):
        if sorted_index[i] < sorted_index[i - 1]:
            return sorted_index[i - 1]
    return -1

