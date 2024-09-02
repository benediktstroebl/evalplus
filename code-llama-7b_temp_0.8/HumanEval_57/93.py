

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Good answer:
    # return sorted(l) == l
    # Monotonic decreasing, or monotonic increasing, or strictly monotonic (non-decreasing or non-increasing)
    if not l:
        return True
    elif len(l) == 1:
        return True
    elif all(x <= y for x, y in zip(l, l[1:])):
        return True
    elif all(x >= y for x, y in zip(l, l[1:])):
        return True
    elif all((x <= y or x >= y) for x, y in zip(l, l[1:])):
        return True
    return False

