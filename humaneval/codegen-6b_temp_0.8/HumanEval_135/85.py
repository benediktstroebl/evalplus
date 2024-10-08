
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

    def f(i):
        if i == 0:
            return -1

        for j in range(0, i):
            if arr[j] <= arr[i]:
                return j

    return f(len(arr) - 1)

