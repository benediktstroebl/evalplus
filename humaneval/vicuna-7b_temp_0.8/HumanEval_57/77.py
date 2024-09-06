

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
    while head < len(tail) - 1:
        if tail[head] > tail[head + 1]:
            return False
        head += 1
    return True
