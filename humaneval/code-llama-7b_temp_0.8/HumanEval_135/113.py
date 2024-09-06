
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # find the maximum number in the arr
    # make a new array of size (max+1)
    # loop through the arr
    #   create the index for the new array
    #   insert the element at that index
    # return the index in the new array that is not -1

    ## TIME COMPLEXITY: O(n)
    ## SPACE COMPLEXITY: O(n)

    # max element in the arr
    max_num = max(arr)
    # create the new arr
    new_arr = [0] * (max_num + 1)

    # fill the new array
    for element in arr:
        new_index = element - 1
        new_arr[new_index] = element

    # loop through the new arr
    for index, element in enumerate(new_arr):
        if element != 0:
            return index

    # if no non-zero element in new arr, return -1
    return -1

    # return -1

