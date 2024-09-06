

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if len(l) <= 1:
        return True
    i = 1
    while i < len(l) and l[i] == l[i - 1]:
        i += 1
    if i == len(l):
        return True
    if i == 1 or i == len(l) - 1:
        return True
    if l[i] < l[i - 1]:
        while i < len(l) and l[i] == l[i - 1]:
            i += 1
        if i == len(l):
            return True
        if l[i] >= l[i - 1]:
            return False
        return monotonic(l[:i]) and monotonic(l[i:])
    if l[i] > l[i - 1]:
        while i < len(l) and l[i] == l[i - 1]:
            i += 1
        if i == len(l):
            return True
        if l[i] <= l[i - 1]:
            return False
        return monotonic(l[:i]) and monot
