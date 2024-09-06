

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    elif len(l) == 2:
        return (l[0] < l[1]) or (l[0] > l[1])
    else:
        inc = [True if i > j else False for i, j in zip(l[1:], l[:-1])]
        dec = [True if i < j else False for i, j in zip(l[1:], l[:-1])]
        return any(inc) or any(dec)

