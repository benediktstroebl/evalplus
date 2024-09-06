

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 3:
        return True
    is_increasing = None
    for i in range(len(l) - 1):
        if is_increasing is None:
            is_increasing = l[i] < l[i + 1]
        else:
            if l[i] < l[i + 1] and not is_increasing:
                return False
            elif l[i] > l[i + 1] and is_increasing:
                return False
    return True

