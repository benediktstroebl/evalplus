

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Check if elements are monotonically increasing
    if l[1:] == sorted(l[1:]):
        return True
    # Check if elements are monotonically decreasing
    elif l[:-1] == sorted(l[:-1], reverse=True):
        return True
    # Otherwise, return False
    else:
        return False

