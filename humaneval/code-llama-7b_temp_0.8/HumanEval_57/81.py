

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    incr = None

    for i in range(1, len(l)):
        if incr is None:
            incr = l[i] > l[i - 1]
        else:
            if (incr and not l[i] > l[i - 1]) or (not incr and not l[i] < l[i - 1]):
                return False

    return True

