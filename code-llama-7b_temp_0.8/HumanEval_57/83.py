

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    d = None
    for i in range(len(l)-1):
        if d is None:
            d = l[i+1]-l[i]
        if d*(l[i+1]-l[i]) < 0:
            return False
    return True

