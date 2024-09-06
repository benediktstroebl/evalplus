

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    assert len(l) > 0, "Cannot determine whether list is monotonic without any elements"
    # fill in your code here
    return all(x < y for x, y in zip(l, l[1:])) or all(x > y for x, y in zip(l, l[1:]))

