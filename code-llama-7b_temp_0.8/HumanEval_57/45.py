

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 3:
        return True

    # assume there are at least 3 elements
    if l[0] <= l[1] <= l[2]:
        return monotonic(l[1:])
    if l[0] >= l[1] >= l[2]:
        return monotonic(l[1:])
    return False

