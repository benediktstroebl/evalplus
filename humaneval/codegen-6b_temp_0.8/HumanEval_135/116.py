
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    #for a[i] < a[i-1]
    prev, max_ind, max_ij = 0, -1, 0
    arr = numpy.array(arr)
    for i, a in enumerate(arr):
        if a >= prev:
            max_ij = i
            max_ind = max(max_ind, i)
        else:
            prev = a
    return max_ind

