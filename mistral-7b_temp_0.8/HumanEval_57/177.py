

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    prev_elem = l[0]
    for el in l[1:]:
        if (el >= prev_elem and el > 0) or (el <= prev_elem and el < 0):
            prev_elem = el
        else:
            return False
    return True

