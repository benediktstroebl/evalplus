
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def max_index(val):
        max_index = -1
        for i,item in enumerate(arr):
            if item <= val:
                max_index = i
                break
        return max_index
    return max_index

