

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return len(l) > 0 and all(
        l[i] <= l[i+1] if i+1 < len(l) else True
        for i in range(len(l)-1)
        )
