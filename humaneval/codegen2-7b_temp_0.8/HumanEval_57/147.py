

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 0: return True
    if len(l) == 1: return True
    prev = l[0]
    for e in l[1:]:
        if prev <= e: prev = e
        else: return False
    return True
