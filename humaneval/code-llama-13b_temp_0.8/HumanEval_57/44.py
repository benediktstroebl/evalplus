

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    diff_list = [l[i+1] - l[i] for i in range(len(l) - 1)]
    if len(set(diff_list)) == 1:
        return True
    return False

