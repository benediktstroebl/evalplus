

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    length = len(l)
    if length == 0:
        return True
    prev = l[0]
    for i in range(1, length):
        if l[i] <= prev:
            return False
        prev = l[i]
    return True
