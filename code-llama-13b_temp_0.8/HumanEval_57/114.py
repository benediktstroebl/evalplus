

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

    check = all if l[0] <= l[1] else any
    for i in range(1, len(l)):
        if l[i] * l[i - 1] <= 0:
            return False

    return check(l[i] * l[i - 1] > 0 for i in range(1, len(l)))

