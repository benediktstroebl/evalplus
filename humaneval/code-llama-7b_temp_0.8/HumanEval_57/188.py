

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l_orig = l
    inc = True
    for idx, val in enumerate(l_orig[1:]):
        if inc:
            if val < l_orig[idx]:
                inc = False
        else:
            if val > l_orig[idx]:
                inc = True
    return True

