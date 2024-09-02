

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 1:
        return True

    sign = [1]
    sign += list(map(lambda x: 1 if x[0] > x[1] else -1, zip(l[:-1], l[1:])))

    return sign.count(1) <= 1
