

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    mono = True
    for i in range(1, len(l)):
        if (l[i-1] > l[i]):
            mono = False
            break
    for i in range(1, len(l)):
        if (l[i-1] < l[i]):
            mono = False
            break
    return mono

