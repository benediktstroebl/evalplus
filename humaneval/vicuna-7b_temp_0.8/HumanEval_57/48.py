

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    head, tail = 0, l[1:]
    for i in range(1, len(tail)):
        if tail[i] < tail[i-1]:
            return False
        if tail[i] > tail[i-1]:
            return True
        if tail[i] < head:
            return False
    return True
