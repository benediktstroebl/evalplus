
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
    arr_copy = arr.copy()
    arr_copy.reverse()
    for i in range(n-1):
        if arr_copy[i] > arr_copy[i+1]:
            return i+1
    return -1

print(can_arrange([2, 1, 5, 3, 4, 5, 1, 2, 1, 2, 3, 4, 5]))  # 2
print(can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # -1