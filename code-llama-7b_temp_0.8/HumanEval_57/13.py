

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

    for i in l:
        if prev is None:
            prev = i
            continue
        if i > prev:
            increasing = False
        if i < prev:
            decreasing = False
        prev = i

    return (increasing or decreasing)
