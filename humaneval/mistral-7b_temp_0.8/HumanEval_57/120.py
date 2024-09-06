

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

    i, j = 0, 1
    while i < len(l) - 1 and j < len(l):
        if l[i] > l[j]:
            return False
        i, j = i + 1, j + 1
    return True

