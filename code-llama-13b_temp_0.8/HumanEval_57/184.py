

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # TODO: check that this function works correctly
    # TODO: test function
    # TODO: improve function
    # TODO: document function

    if l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                return False
    elif l[0] > l[1]:
        for i in range(1, len(l)):
            if l[i - 1] < l[i]:
                return False
    return True


