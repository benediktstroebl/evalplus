
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Arrays are sorted, so we'll always find our element in the first
    # iteration
    # NOTE: You can write your own test cases for this function if needed,
    # but it is encouraged to use the ones below
    def helper(arr, i):
        if arr[i] > arr[i - 1]:
            return i
        return -1

    return helper(arr, len(arr) - 1)
