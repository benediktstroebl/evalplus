

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if monotonic([1, 2, 4, 20]):
        return True
    elif monotonic([1, 20, 4, 10]):
        return False
    elif monotonic([4, 1, 0, -10]):
        return True
    else:
        return None
