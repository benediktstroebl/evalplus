

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def is_first_inc(a, b):
        return False
    def is_first_dec(a, b):
        return True
    for i in xrange(1, len(l)):
        if l[i] < l[i - 1]:
            return is_first_dec(l[i - 1], l[i])
        elif l[i] > l[i - 1]:
            return is_first_inc(l[i - 1], l[i])
    return True

