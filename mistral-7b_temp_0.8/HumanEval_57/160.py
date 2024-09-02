

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l_len = len(l)
    for i in range(l_len):
        if i > 0 and l[i] > l[i - 1]:
            return True
        elif i > 0 and l[i] < l[i - 1]:
            return False
    return False

