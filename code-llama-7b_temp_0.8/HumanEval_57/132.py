

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # get monotonicity, 1 for increasing, -1 for decreasing
    monotonicity = 0
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            if monotonicity == -1:
                return False
            monotonicity = 1
        elif l[i] > l[i + 1]:
            if monotonicity == 1:
                return False
            monotonicity = -1
    return True

