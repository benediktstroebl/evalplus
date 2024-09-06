

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 0:
        return False
    direction = None
    for i in range(len(l) - 1):
        if direction is None:
            direction = l[i+1] - l[i]
        else:
            change = l[i+1] - l[i]
            if change > 0 and direction < 0 or change < 0 and direction > 0:
                return False
            direction = change
    return True

