

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def _mono(increasing: bool):
        return all(b - a <= 0 if increasing else b - a >= 0
                   for a, b in zip(l[:-1], l[1:]))

    return _mono(False) or _mono(True)

