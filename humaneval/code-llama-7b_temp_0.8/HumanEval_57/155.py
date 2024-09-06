

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    is_decreasing = None
    prev = l[0]
    for i in l:
        if is_decreasing is None:
            is_decreasing = i < prev
        if is_decreasing:
            if i > prev:
                return False
        else:
            if i < prev:
                return False
        prev = i
    return True

