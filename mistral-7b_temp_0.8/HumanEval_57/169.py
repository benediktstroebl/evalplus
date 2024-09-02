

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    assert type(l) is list, "expected a list, got: %s" % type(l)
    assert len(l) > 0, "list must have at least one element"
    prev = l[0]
    for i in l[1:]:
        if prev < i:
            prev = i
        else:
            return False
    return True

