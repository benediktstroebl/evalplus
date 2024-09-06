

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # For sorted list, there will be no decreasing items
    # For reverse sorted list, there will be no increasing items

    prev = l[0]
    for n in l[1:]:
        if prev < n:
            prev = n
        else:
            return False
    return True

