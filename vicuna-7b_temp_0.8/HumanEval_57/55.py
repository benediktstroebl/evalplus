

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    from .stats import stats
    from . import numeric
    u, lo, hi = stats(l)
    if lo == lo[0]:
        return True
    if lo == hi:
        return not u.is_integer()
    return not u.is_integer() or lo <= u <= hi
