

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    assert len(l) > 0, "List must be non-empty"
    curr, next = l[0], l[1]
    if curr < next:
        return monotonic(l[1:])
    elif curr > next:
        return not monotonic(l[1:])
    else:
        return True
