

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    diff = None
    for i in range(1, len(l)):
        if diff is None:
            diff = l[i] - l[i - 1]
        else:
            new_diff = l[i] - l[i - 1]
            if new_diff * diff < 0:
                return False
            diff = new_diff
    return True
