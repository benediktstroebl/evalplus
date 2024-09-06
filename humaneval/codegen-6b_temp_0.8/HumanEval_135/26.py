
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def can(curr, prev):
        if prev == None:
            return True
        elif prev < curr:
            return True
        else:
            return False

    if len(arr) < 2:
        return -1
    else:
        prev = arr[0]
        for i in range(1, len(arr)):
            if not can(arr[i], prev):
                return i
            prev = arr[i]
        return -1

"""
OPTIONAL SOLUTION
"""
