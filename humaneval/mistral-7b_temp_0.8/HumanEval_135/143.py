
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_s = set(arr)
    lst = list(arr_s)
    lst.sort()
    if len(arr) == len(lst):
        return arr.index(lst[len(lst) - 1])
    else:
        return -1








