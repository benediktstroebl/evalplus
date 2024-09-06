

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 1 or len(l) == 2:
        return True
    f = lambda x, y: x <= y
    if l[0] < l[1]:
        f = lambda x, y: x >= y

    for i in range(len(l)-1):
        if f(l[i], l[i+1]) == False:
            return False

    return True

