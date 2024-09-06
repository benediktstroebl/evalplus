

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 1:
        return True
    if l[0] >= l[1]:
        return all(prev >= item for prev, item in zip(l, l[1:]))
    else:
        return all(prev <= item for prev, item in zip(l, l[1:]))

