

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

    res = []
    for i in range(len(l) - 1):
        if l[i + 1] - l[i] < 0:
            return False
        else:
            res.append(l[i + 1] - l[i])

    if res == sorted(res, reverse=True):
        return True
    else:
        return False

