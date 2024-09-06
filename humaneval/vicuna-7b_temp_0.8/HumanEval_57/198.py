

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def monotonic_indices(l):
        for i, v in enumerate(l):
            if v > l[i-1]:
                return False
            elif v < l[i-1]:
                return True
        return True

    return monotonic_indices(l)
