

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def is_monotonic(a: int, b: int, mode: int) -> bool:
        return (a <= b) == (mode == 0)
    
    def monotonicity(l: list, mode: int) -> bool:
        return all(is_monotonic(a, b, mode) for a, b in zip(l, l[1:]))

    return any(monotonicity(l, mode) for mode in [0, 1])
