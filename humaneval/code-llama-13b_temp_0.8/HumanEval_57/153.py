

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def _monotonic(l):
        if len(l) == 1:
            return True
        elif l[0] < l[1]:
            return _monotonic(l[1:])
        elif l[0] > l[1]:
            return not _monotonic(l[1:])
        else:
            return _monotonic(l[1:])
    return _monotonic(l) or _monotonic(l[::-1])
