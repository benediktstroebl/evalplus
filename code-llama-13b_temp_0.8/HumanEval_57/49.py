

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

    def _monotonic_helper(l, inc):
        if inc:
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    return False
        else:
            for i in range(len(l) - 1):
                if l[i] < l[i + 1]:
                    return False
        return True

    if l[0] < l[-1]:
        return _monotonic_helper(l, True)
    else:
        return _monotonic_helper(l, False)

