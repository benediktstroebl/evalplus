

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    diffs = [y - x for x, y in zip(l[:-1], l[1:])]
    return all(diffs[i] <= 0 for i in range(len(diffs) - 1)) or all(
        diffs[i] >= 0 for i in range(len(diffs) - 1)
    )

