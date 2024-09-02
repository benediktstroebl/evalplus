

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = None
    for i in range(len(l) - 1):
        a, b = l[i:i+2]
        if increasing is None and a < b:
            increasing = True
        elif decreasing is None and a > b:
            decreasing = True
        if increasing and b < a:
            return False
        if decreasing and b > a:
            return False
    return True
