

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    delta = 0
    for i in range(len(l) - 1):
        delta = l[i + 1] - l[i]
        if delta > 0:
            for j in range(i + 1, len(l) - 1):
                if l[j + 1] - l[j] > 0:
                    continue
                else:
                    return False
        if delta < 0:
            for j in range(i + 1, len(l) - 1):
                if l[j + 1] - l[j] < 0:
                    continue
                else:
                    return False
    return True

