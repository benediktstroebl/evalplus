

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    first_diff = max(l) - min(l)
    second_diff = (max(l[1:]) - min(l[1:])) if len(l) > 1 else 0
    return (first_diff < 0) or ((first_diff == 0 and second_diff > 0) or (first_diff == 0 and second_diff == 0))