

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increase = None
    for i in range(len(l) - 1):
        if increase is None:
            increase = l[i] <= l[i+1]
        elif increase:
            if l[i] > l[i+1]:
                return False
        else:
            if l[i] < l[i+1]:
                return False
    return True

