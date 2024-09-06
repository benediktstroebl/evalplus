

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 2:
        return True
    direction = 0
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            continue
        if direction == 0:
            direction = 1 if l[i] < l[i + 1] else -1
        else:
            if (l[i] < l[i + 1] and direction != 1) or (l[i] > l[i + 1] and direction != -1):
                return False
    return True

