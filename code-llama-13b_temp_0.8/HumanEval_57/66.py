

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True
    i = 0
    m = l[0] - l[1]
    while i < len(l) - 1:
        x = l[i]
        y = l[i + 1]
        if m > 0:
            if y - x < 0:
                return False
        elif m < 0:
            if y - x > 0:
                return False
        else:
            return False
        i += 1
    return True

