
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # create a dictionary to store the index for each value
    indices = {}

    # iterate through each element in the array
    for i in range(len(arr)):

        # if the current element is not in the dictionary add it and its index
        if arr[i] not in indices:
            indices[arr[i]] = i

    # iterate through each element in the array again
    for i in range(len(arr)):

        # if the current element is greater than or equal to the previous one
        # return the index of the previous element
        if arr[i] >= arr[i-1]:
            return indices[arr[i-1]]

    # if the array is decreasing then return -1
    return -1
