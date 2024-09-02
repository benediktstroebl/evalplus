

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
    for idx, element in enumerate(l[1:]):
        if increasing and not element >= l[idx]:
            increasing = False
        if decreasing and not element <= l[idx]:
            decreasing = False
    return increasing or decreasing
