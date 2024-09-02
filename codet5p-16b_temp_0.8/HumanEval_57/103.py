

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    n = len(l)
    if n > 1:
        if l[0] <= l[1]:
            increasing = monotonic(l[1:])
        else:
            increasing = False
        if increasing and l[n - 1] <= l[n - 2]:
            decreasing = monotonic(l[:n - 1])
        else:
            decreasing = False
    else:
        return True
    return increasing or decreasing
    
