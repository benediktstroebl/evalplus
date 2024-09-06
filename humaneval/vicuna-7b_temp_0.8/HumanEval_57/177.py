

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l_rev = list(reversed(l))
    for i in range(len(l)):
        if l[i] > l[i+1]:
            return False
        elif l[i] < l[i+1]:
            return True
        elif l[i] == l[i+1]:
            if l_rev[i+1] > l_rev[i]:
                return False
    return True