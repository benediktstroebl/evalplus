

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def is_monotonic(i):
        return all(x >= y for j, x, y in zip(range(i + 1, len(l)), l[i:], l[i + 1:])) or \
            all(x <= y for j, x, y in zip(range(i + 1, len(l)), l[i:], l[i + 1:]))

    return all(is_monotonic(i) for i in range(len(l)))
