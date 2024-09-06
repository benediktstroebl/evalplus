

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    diffs = []
    for i in range(1, len(l)):
        diffs.append(l[i] - l[i - 1])

    # If list elements are monotonically increasing:
    if all(diff > 0 for diff in diffs):
        return True
    # If list elements are monotonically decreasing:
    if all(diff < 0 for diff in diffs):
        return True

    return False

