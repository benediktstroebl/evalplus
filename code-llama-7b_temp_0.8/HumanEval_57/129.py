

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if not l:
        return False
    m = None
    for e in l:
        if m is None:
            m = e
            continue
        if e < m:
            return False
        m = e
    return True

