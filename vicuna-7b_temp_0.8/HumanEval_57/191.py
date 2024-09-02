

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    last = l[-1]
    for i, elt in enumerate(reversed(l[:-1])):
        if elt > last:
            return False
        if elt < last:
            return True
    return True
