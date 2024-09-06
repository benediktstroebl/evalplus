

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Bad
    if len(l) == 1:
        return True
    i = 1
    direction = 0
    while i < len(l):
        if l[i] > l[i - 1]:
            if direction == -1:
                return False
            if direction == 0:
                direction = 1
        elif l[i] < l[i - 1]:
            if direction == 1:
                return False
            if direction == 0:
                direction = -1
        else:
            return False
        i += 1
    return True

