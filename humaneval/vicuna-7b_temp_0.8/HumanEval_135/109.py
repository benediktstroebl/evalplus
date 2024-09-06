
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not is_sorted(arr):
        return -1
    
    n = len(arr)
    arr_1 = arr[1:n]
    arr_2 = arr[:n-1]
    max_index = 0
    for i in range(1, n):
        if arr_1[i] <= arr_2[i-1]:
            max_index = i
            break
    if max_index == 0:
        return -1
    else:
        return max_index