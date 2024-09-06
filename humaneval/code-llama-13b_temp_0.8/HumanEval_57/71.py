

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def inc(a, b):
        return a < b

    def dec(a, b):
        return a > b

    if not l:
        return True

    op = inc if l[0] < l[1] else dec
    for i in range(1, len(l)):
        if op(l[i - 1], l[i]):
            continue
        return False
    return True

