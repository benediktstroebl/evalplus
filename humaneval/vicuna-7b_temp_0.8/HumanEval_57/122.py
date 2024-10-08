

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l.reverse()
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i += 1
    return True
