

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    def is_decreasing(l: list):
        return all(l[i] >= l[i + 1] for i in range(len(l) - 1))

    def is_increasing(l: list):
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    if is_decreasing(l) or is_increasing(l):
        return True
    return False
