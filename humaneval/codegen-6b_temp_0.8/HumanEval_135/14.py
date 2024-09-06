
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    previous = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= previous:
            return i - 1
        previous = arr[i]
    return -1


assert(can_arrange([1, 2, 4, 3, 5]) == 3)
assert(can_arrange([1, 2, 3]) == -1)
assert(can_arrange([1, 2, 3, 4, 5]) == -1)
assert(can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1)
assert(can_arrange([1, 2, 3, 4, 5, 5, 6, 7, 8, 9]) == -1)
assert(can_arrange([7, 8, 9]) == -1)
assert(can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1)
assert(can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1)
assert(can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1)
assert(can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == -1)