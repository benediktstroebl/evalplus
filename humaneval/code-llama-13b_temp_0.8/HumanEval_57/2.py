

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    prev = None
    decreasing = None
    for x in l:
        if prev is None:
            prev = x
        elif x == prev:
            continue
        elif decreasing is None:
            decreasing = x < prev
        elif decreasing:
            if x < prev:
                prev = x
            else:
                return False
        else:
            if x > prev:
                prev = x
            else:
                return False
    return True

