

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if all(a <= b for a, b in zip(l[::2], l[1::2])) or all(a >= b for a, b in zip(l[::2], l[1::2])):
        return True
    else:
        return False
