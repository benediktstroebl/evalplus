

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True

    order = 1 if l[1] - l[0] > 0 else -1 if l[1] - l[0] < 0 else 0

    if order == 0:
        return False

    for i in range(2, len(l)):
        if (l[i] - l[i - 1]) * order < 0:
            return False

    return True

