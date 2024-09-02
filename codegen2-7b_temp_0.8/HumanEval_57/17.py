

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(map(lambda i, j: i < j, l, l[1:])) and \
        all(map(lambda i, j: j > i, l, l[1:]))
