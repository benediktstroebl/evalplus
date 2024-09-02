

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
    i = 0
    while i < len(l) - 1:
        if l[i + 1] > l[i]:
            i += 1
        elif l[i + 1] == l[i]:
            i += 1
        else:
            return False
    return True
