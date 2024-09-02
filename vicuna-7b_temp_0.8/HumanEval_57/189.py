

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    first = next(iter(l))
    for i, el in enumerate(l[1:], 1):
        if el < first:
            return False
        elif el > first:
            return True
    return True