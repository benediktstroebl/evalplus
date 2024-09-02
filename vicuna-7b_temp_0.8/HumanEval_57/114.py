

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # sort elements
    l = sorted(l)
    
    # check if elements are strictly monotonically increasing or decreasing
    return l[1] <= l[0] or l[-1] >= l[-2]
