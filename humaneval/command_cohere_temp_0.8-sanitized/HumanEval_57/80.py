def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = set(l)
    return all(x <= y or x >= y == len(a) == 1 for x, y in zip(l, l[1:]))