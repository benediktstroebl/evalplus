

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    inc_check = l[0] <= l[1] <= l[2]
    dec_check = l[0] >= l[1] >= l[2]
    return inc_check or dec_check

