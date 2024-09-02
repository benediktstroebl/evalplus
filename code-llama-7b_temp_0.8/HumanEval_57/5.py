

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 1:
        return True
    if len(l) == 2:
        return l[0] == l[1] or l[0] < l[1] or l[0] > l[1]
    first = l[0]
    for i in l:
        if first < i:
            first = i
        if first > i:
            return False
    return True

