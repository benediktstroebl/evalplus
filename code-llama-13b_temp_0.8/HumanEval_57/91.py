

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    direction = 0
    for i in range(len(l) - 1):
        diff = l[i + 1] - l[i]
        if direction == 0:
            if diff > 0:
                direction = 1
            elif diff < 0:
                direction = -1
        if direction == 1:
            if diff < 0:
                return False
        if direction == -1:
            if diff > 0:
                return False
    return True
