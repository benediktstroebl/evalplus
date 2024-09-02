

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
    elif l[1] == l[0]:
        return True
    elif l[1] > l[0]:
        if all(l[i] <= l[i + 1] for i in range(len(l) - 1)):
            return True
    elif l[1] < l[0]:
        if all(l[i] >= l[i + 1] for i in range(len(l) - 1)):
            return True
    return False

