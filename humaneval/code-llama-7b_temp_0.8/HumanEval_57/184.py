

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # If list is empty, return True.
    if len(l) < 2:
        return True

    # Get sign of difference.
    sign = (l[0] - l[1]) / abs(l[0] - l[1])

    # Check if other differences have the same sign.
    for i in range(1, len(l) - 1):
        if (l[i] - l[i + 1]) * sign <= 0:
            return False
    return True

