

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    prev_i = l[0]
    prev_d = prev_i - l[1]
    for i in range(1, len(l)):
        if (prev_d * (l[i] - prev_i) > 0):
            return False
        prev_i = l[i]
        prev_d = l[i] - prev_i
    return True

