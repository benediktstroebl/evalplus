

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 3:
        return True

    if l[0] > l[1]:
        if l[2] > l[1]:
            return monotonic(l[3:])
        else:
            return False

    elif l[0] < l[1]:
        if l[2] < l[1]:
            return monotonic(l[3:])
        else:
            return False

    else:
        return True


