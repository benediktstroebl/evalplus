

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = True
    decreasing = True
    prev = None

    for x in l:
        if prev is None:
            prev = x
            continue
        if increasing and x < prev:
            increasing = False
        elif decreasing and x > prev:
            decreasing = False
        prev = x

    return increasing or decreasing
