

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True
    if l[1] - l[0] == 0:
        return monotonic(l[1:])
    return (all(l[i+1] - l[i] > 0 for i in range(len(l)-1)) or
            all(l[i+1] - l[i] < 0 for i in range(len(l)-1)))

