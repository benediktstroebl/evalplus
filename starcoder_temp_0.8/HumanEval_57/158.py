

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    return all(a <= b for a, b in zip(l[:-1], l[1:])) or all(a >= b for a, b in zip(l[:-1], l[1:]))

