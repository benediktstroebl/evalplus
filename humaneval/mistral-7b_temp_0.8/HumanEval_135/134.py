
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Write your code here.
    # NOTE: In Python a list can be accessed by using an index, e.g. arr[0]
    # accesses the first element of the array arr.

    # Initially, we assume that we have found the largest index.
    largest_index = len(arr)
    # Loop over the array.
    for index, element in enumerate(arr):
        # If the element is not greater than or equal to the element preceding it
        if element < arr[index-1]:
            # Update the largest index.
            largest_index = index
    return largest_index

