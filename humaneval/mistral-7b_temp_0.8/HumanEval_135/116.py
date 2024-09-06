
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # To solve this problem we need to make a list of arrays which are
    # (2*n + 1) elements long where we push the elements of the given array
    # into the first n spots and then we fill up the remaining spots with
    # zeros.

    # We then iterate through these arrays, starting at the second element
    # and working our way back to the first element. If we find a 0 in an
    # element and the previous element is greater than or equal to the current
    # element, we can return the index of the element in which the 0 was
    # found.

    # If we never find a 0 that is greater than or equal to the element
    # immediately preceding it, we can return -1 to indicate that such an
    # element does not exist.

    # For example, the array [1,2,3] would yield the following arrays:

    # [[1,2,3,0,0,0,0,0,0], [0,1,2,0,3,0,0,0,0], [0,0,1
