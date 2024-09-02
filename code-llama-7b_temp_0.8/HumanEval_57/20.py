

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # let's compare the current element with the previous
    # if they're not of the same sign, then it is not monotonic
    # otherwise, do nothing
    if len(l) < 2:
        return True

    sign = 0
    for i in range(1, len(l)):
        if l[i-1] * l[i] < 0:
            sign = sign + 1
        if sign == 2:
            return False

    return True

