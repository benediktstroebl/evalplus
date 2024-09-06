
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def helper(arr, max_index):
        if len(arr) == 0:
            return max_index
        if arr[0] <= arr[1]:
            return helper(arr[1:], max_index)

        return helper(arr[1:], max(max_index, 1))

    return helper(arr, 0)[0]



assert can_arrange([1,2,4,3,5]) == 3
assert can_arrange([1,2,3]) == -1
