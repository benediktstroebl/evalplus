

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
    elif len(l) == 2:
        return l[0] <= l[1]

    i = 1
    while i < len(l):
        if (l[i-1] > l[i]) or (l[i-1] < l[i]):
            return False
        i += 1
    return True

