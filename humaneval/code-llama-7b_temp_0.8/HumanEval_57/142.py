

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    assert len(l) > 0
    if len(l) == 1:
        return True

    last = l[0]
    for x in l[1:]:
        if last > x:
            return False
        last = x
    return True

