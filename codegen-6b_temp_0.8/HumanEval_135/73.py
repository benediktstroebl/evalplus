
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    index_dict = {x:arr.index(x) for x in arr}
    for j, i in enumerate(arr):
        if index_dict[i] <= index_dict[i - 1]:
            return -1
    return len(arr) - 1

