

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def incr(e1, e2):
        return e1 <= e2

    def decr(e1, e2):
        return e1 >= e2

    m = l[0]
    for e in l[1:]:
        if (incr(m, e) or decr(m, e)):
            m = e
        else:
            return False
    return True
