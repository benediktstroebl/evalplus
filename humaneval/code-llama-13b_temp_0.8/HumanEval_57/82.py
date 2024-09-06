

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def _increasing(l):
        for i in range(len(l) - 1):
            if l[i + 1] < l[i]:
                return False
        return True

    def _decreasing(l):
        for i in range(len(l) - 1):
            if l[i + 1] > l[i]:
                return False
        return True

    return _increasing(l) or _decreasing(l)

