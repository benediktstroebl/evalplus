

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    diffs = [l[i] - l[i - 1] for i in range(1, len(l))]
    is_increasing = all(diffs[i] >= 0 for i in range(len(diffs)))
    is_decreasing = all(diffs[i] <= 0 for i in range(len(diffs)))
    return is_increasing or is_decreasing

