

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # 'cmp' is not available in Python 3
    # cmp(a, b) returns -1 if a<b
    # cmp(a, b) returns 1 if a>b
    # So, we use a>b instead of a<b
    return all(a <= b for a, b in zip(l[1:], l[:-1])) or all(
        a >= b for a, b in zip(l[1:], l[:-1]))

