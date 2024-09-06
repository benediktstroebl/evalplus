def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = set(l[0:len(l) // 2])
    b = set(l[len(l) // 2:])
    return len(a | b) <= 1