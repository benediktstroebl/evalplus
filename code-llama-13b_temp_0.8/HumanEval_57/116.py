

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    sign = lambda x: (1, -1)[x < 0]
    if len(l) <= 1:
        return True
    s = sign(l[1] - l[0])
    for i in range(2, len(l)):
        if sign(l[i] - l[i-1]) != s:
            return False
    return True
