
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    arr_rev = [arr[n-i-1] for i in range(n)]
    arr_rev_sort = sorted(arr_rev)
    index = 0
    while arr_rev_sort[index] < arr_rev_sort[index-1] and index < n-1:
        index += 1
    if index == n-1:
        return -1
    return index
