

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    sign = 1
    for x in l:
        if sign != 0:
            if x < 0:
                sign = -1
            elif x > 0:
                sign = 1
        else:
            return False
    return True

