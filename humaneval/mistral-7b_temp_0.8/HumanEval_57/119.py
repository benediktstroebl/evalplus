

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def helper(l):
        if len(l) < 2:
            return True
        return l[0] < l[1] and helper(l[1:]) or l[0] > l[1] and helper(l[1:])

    return helper(l)

