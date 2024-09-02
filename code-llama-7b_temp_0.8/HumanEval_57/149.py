

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l = list(l)
    l.sort()
    return l == list(range(l[0], l[-1] + 1)) or l == list(range(l[0], l[-1] - 1, -1))

