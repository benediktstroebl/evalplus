
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    from collections import deque
    d = deque([])
    for num in arr:
        d.append(num)
        while d[-1] >= d[0]:
            d.popleft()
    if len(d) > 0:
        return arr.index(d[0])
    else:
        return -1
