

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    current = l[0]
    for val in l[1:]:
        if current > val:
            return False
        elif current < val:
            return True
        current = val
    return True
