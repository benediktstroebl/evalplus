

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    d = 0
    for i in range(1, len(l)):
        if l[i-1] < l[i]:
            d = 1
        elif l[i-1] > l[i]:
            d = -1
        if d != 0 and d != (l[i] - l[i-1]):
            return False
    return True
