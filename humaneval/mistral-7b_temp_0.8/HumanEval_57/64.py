

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == []:
        return True
    # check the first element
    if l[0] > l[1]:
        return False

    for i in range(len(l) - 2):
        if l[i] > l[i + 2]:
            return False
    return True

