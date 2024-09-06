

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    is_increasing = l[0] < l[-1]
    return all(
        (e < e2 if is_increasing else e > e2) for e, e2 in zip(l, l[1:]))

