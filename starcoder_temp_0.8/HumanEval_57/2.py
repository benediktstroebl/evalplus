

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
    inc = l[1] - l[0] > 0
    for i in range(1, len(l)):
        if inc and l[i] - l[i-1] < 0:
            return False
        if not inc and l[i] - l[i-1] > 0:
            return False
    return True
