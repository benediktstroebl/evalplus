

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    for index, item in enumerate(l):
        if index > 0 and l[index] != l[index-1]:
            if l[index] < l[index-1]:
                return False
            else:
                return True
    return False
