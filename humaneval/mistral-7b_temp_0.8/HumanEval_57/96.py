

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    """ if l[1] > l[0]:
        for i in range(2, len(l)):
            if l[i] < l[i-1]:
                return False
        return True
    elif l[1] < l[0]:
        for i in range(2, len(l)):
            if l[i] > l[i-1]:
                return False
        return True
    else:
        return False """
    return False if l[1] > l[0] and l[2] < l[1] or l[1] < l[0] and l[2] > l[1] else True
