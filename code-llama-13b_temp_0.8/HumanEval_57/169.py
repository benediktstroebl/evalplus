

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def is_increasing():
        return all(l[i - 1] <= l[i] for i in range(1, len(l)))

    def is_decreasing():
        return all(l[i - 1] >= l[i] for i in range(1, len(l)))

    return is_increasing() or is_decreasing()
