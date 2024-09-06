

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # monotonicity can be tested on a list
    # by testing whether it is sorted in
    # either ascending or descending order

    # test ascending order first
    if l == sorted(l):
        return True
    # if not ascending, test descending
    elif l == sorted(l, reverse=True):
        return True
    else:
        return False

