
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    lst = arr[::-1]
    max_index = 0
    for i in range(len(lst)):
        if lst[i] <= lst[i-1]:
            max_index = i

    if max_index == len(lst):
        return -1
    else:
        return lst.index(lst[max_index])
