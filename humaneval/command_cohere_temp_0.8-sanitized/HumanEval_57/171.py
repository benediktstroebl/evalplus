def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = b = float(l[1])
    for x in l[1:]:
        if x < a:
            return False
        if x > b:
            return False
        a = b
        b = x
    return True