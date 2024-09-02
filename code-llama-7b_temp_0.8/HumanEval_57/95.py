

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    flag = True
    l_len = len(l)
    for i in range(l_len - 1):
        if l[i] > l[i + 1]:
            flag = False
        elif l[i] < l[i + 1]:
            flag = True
    return flag

