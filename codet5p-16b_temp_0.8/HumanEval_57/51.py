

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if not l: return True
    if len(l) == 1: return True
    if len(l) == 2:
        return l[0] <= l[1]
    return (l[0] <= l[1] and monotonic(l[1:])) or (l[0] >= l[1] and monotonic(l[1:][::-1]))
