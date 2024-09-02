

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
    if l_len <= 1:
        return True
    a = l[0]
    b = l[1]
    if b > a:
        for i in range(2, l_len):
            if l[i] < b:
                return False
            b = l[i]
    else:
        for i in range(2, l_len):
            if l[i] > b:
                return False
            b = l[i]
    return True
