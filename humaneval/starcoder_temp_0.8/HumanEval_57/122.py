

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l[1] > l[0]:
        return all(e1 <= e2 for e1, e2 in zip(l[:-1], l[1:]))
    elif l[1] < l[0]:
        return all(e1 >= e2 for e1, e2 in zip(l[:-1], l[1:]))
    else:
        return False
