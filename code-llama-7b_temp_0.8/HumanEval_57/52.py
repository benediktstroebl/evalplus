

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Get first element and set sign.
    sign = -1
    if l[0] < l[1]:
        sign = 1
    diff = sign * (l[0] - l[1])
    # check if other elements are increasing or decreasing
    # with same sign.
    for i in range(1, len(l) - 1):
        if sign * (l[i] - l[i + 1]) != diff:
            return False
    return True

