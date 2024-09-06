

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
    diff = [l[i] - l[i-1] for i in range(1, len(l))]
    sign = 0
    for d in diff:
        if sign == 0:
            if d == 0:
                continue
            sign = 1 if d > 0 else -1
        elif sign == 1:
            if d > 0:
                continue
            else:
                return False
        elif sign == -1:
            if d < 0:
                continue
            else:
                return False
        else:
            raise RuntimeError
    return True

