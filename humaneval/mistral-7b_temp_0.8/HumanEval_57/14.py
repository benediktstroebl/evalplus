

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    assert isinstance(l, list), "Argument should be a list"
    return all([l[i] == l[0] or l[i] > l[i-1] for i in range(1, len(l))])
