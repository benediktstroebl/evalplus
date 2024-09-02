

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True

    # 20:30 20:50
    previous = l[0]
    for i in range(1, len(l)):
        if l[i] == previous:
            return False
        if l[i] > previous:
            previous = l[i]
        else:
            previous = l[i]
    return True


