

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Create a monotonic increasing function, which is # the opposite of the
    # monotonic decreasing function
    def maior(a, b): return a if a > b else b
    return all(maior(a, b) <= maior(b, c) for a, b, c in zip(l, l[1:], l[2:]))

