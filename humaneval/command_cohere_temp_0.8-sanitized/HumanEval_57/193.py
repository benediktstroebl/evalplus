def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = set(l[0:-1])
    b = set(l[1:])
    return len(a | b) <= 1