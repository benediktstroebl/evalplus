
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # check for a linear relationship between elements in the array
    # if there is, then there will be a value which is not greater than
    # or equal to the value immediately preceding it
    # i.e. if i = 1, 2, 3, 4, 5 then there is a linear relationship
    # if i = 1, 2, 2, 3, 4 then there is not a linear relationship
    # if i = 1, 1, 2, 2, 3 then there is not a linear relationship
    #
    # We're going to do a lot of checking, but we're going to use a dict to
    # make sure we're checking each element just once.
    #
    # This means we'll check the same element multiple times, so we'll need to
    # store the result of the checks in a variable.

    # make sure arr is not empty
    if len(arr) == 0:
        return -1

    # if arr has just one element then that element is not greater than or
    # equal to anything preceding it, so return it
    if len(arr) == 1:
        return 0

    # make sure that arr has more than one element, and has no duplicate
    # values
    elements = {}
    for i in range(len(arr)):
        if arr[i] in elements:
            return -1
        elements[arr[i]] = 1

    # now that we know that arr has at least two elements and that it contains
    # no duplicate values, loop through each element in arr.
    #
    # We're going to start at the second element in arr because the first
    # element in arr, if it's greater than the second element in arr then we
    # know that arr doesn't contain a linear relationship, so we'll return -1
    # immediately.
    #
    # We'll be returning the index of the last element in arr which is not
    # greater than or equal to the preceding element, so we'll keep track of
    # this index with the variable 'largest'.
    largest = -1
    for i in range(1, len(arr)):
