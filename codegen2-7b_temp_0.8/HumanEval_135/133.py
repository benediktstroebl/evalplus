
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def can_arrange_helper(arr):
        max_index = -1
        for i in range(len(arr)):
            if arr[i] >= arr[i + 1] and arr[i] > max_index:
                max_index = arr[i]
        return max_index

    return can_arrange_helper(arr
