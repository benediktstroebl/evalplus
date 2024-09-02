

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    expected = 1
    for i in range(len(l) - 1):
        if l[i + 1] != l[i]:
            expected = 0 if expected == 1 else 1
    return expected
