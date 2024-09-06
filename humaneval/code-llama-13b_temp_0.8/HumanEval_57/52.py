

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 2:
        return True
    direct = l[1] - l[0]
    for i in range(len(l)-1):
        if (l[i+1] - l[i]) * direct < 0:
            return False
    return True
