

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l = l.copy()
    l.sort()
    return all(a >= b for a, b in zip(l, l[1:])) or all(a <= b for a, b in zip(l, l[1:]))

