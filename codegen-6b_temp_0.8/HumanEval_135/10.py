
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Define f(i) to be the result of the largest index j > i such that
    # arr[j] <= arr[i]. If f(i) < i, we have arr[j] > arr[i], so the
    # result is i.
    def f(i):
        for j in range(i, -1, -1):
            if arr[j] <= arr[i]:
                return j
        return -1
    i = 0
    while i < len(arr) - 1:
        if f(i) == -1:
            return -1
        i += 1
    return i


TESTING = True