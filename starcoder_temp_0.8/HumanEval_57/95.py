

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    prev, sign = None, None
    for x in l:
        if prev is None:
            prev = x
            continue
        cur_sign = cmp(x, prev)
        if sign is None:
            sign = cur_sign
            continue
        if cur_sign!= sign:
            return False
        prev = x
    return True

