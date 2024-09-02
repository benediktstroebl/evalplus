

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def inc(l: list):
        prev = None
        for i in l:
            if prev and prev > i:
                return False
            prev = i
        return True

    def dec(l: list):
        prev = None
        for i in l:
            if prev and prev < i:
                return False
            prev = i
        return True

    if inc(l) or dec(l):
        return True
    else:
        return False



