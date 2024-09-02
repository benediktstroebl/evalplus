
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1

    sorted_arr = sorted(arr)

    def max_previous(i):
        if i == 0:
            return -1

        if sorted_arr[i] <= sorted_arr[i-1]:
            return -1

        return arr.index(sorted_arr[i-1])
    return max_previous
