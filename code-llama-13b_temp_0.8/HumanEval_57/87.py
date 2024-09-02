

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    sign = lambda x: 0 if x == 0 else x // abs(x)
    s = sign(l[1] - l[0]) if len(l) > 1 else 0
    return all(sign(l[i] - l[i - 1]) == s for i in range(1, len(l)))

