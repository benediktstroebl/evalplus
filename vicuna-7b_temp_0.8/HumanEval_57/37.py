

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    seen = set()
    i = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            seen.add(l[i])
            i += 1
        elif l[i] < l[i + 1]:
            if l[i] in seen:
                return False
        else:
            seen.add(l[i])
            i += 1
    if l[i] == l[i + 1]:
        return False
    return True
