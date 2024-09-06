

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    l_len = len(l)
    if l_len == 0:
        return False
    elif l_len == 1:
        return True
    else:
        i = 0
        while i < l_len - 1:
            if l[i] == l[i + 1]:
                return False
            elif l[i] < l[i + 1]:
                i += 1
            else:
                return False
        return True

