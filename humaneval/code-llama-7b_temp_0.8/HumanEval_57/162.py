

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Your code here
    if len(l) < 2:
        return True
    mon = l[0]
    for x in l[1:]:
        if x == mon:
            return False
        if mon > x and mon - x > 0:
            return False
        if mon < x and x - mon > 0:
            return False
        mon = x
    return True

