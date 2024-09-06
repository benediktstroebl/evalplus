
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # init our pointer
    ptr = 0
    # we want to iterate up to 1 element from the end
    upper = len(arr) - 1
    # init our answer
    answer = -1
    # iterate over the list
    while ptr < upper:
        # if our current element is <= the next element, set answer
        if arr[ptr] <= arr[ptr + 1]:
            answer = ptr + 1
        # otherwise, the element is too big, move our pointer back
        else:
            ptr = answer
        # move our pointer
        ptr += 1
    return answer

