

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

    is_incr = l[0] <= l[1]
    for i in range(1, len(l)-1):
        if is_incr and l[i] <= l[i+1]:
            pass
        elif not is_incr and l[i] >= l[i+1]:
            pass
        else:
            return False
    return True

