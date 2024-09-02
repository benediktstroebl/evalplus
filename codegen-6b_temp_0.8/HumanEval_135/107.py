
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def one_away(i):
        if i == -1 or i == len(arr) - 1:
            return -1
        for j in range(i + 1, len(arr)):
            if arr[i] <= arr[j]:
                return j
        return -1
    return one_away

