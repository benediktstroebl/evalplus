
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

    # a[i] is the largest element that is not greater than or equal to
    # a[i - 1]
    a = arr.copy()
    a.sort()
    for i, _ in enumerate(a):
        if a[i] <= a[i - 1]:
            return -1
        elif i == len(a) - 1 or a[i] >= a[i + 1]:
            return i

    return -1

