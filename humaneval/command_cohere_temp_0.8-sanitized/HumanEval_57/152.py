def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, d = float('-inf'), float('inf'), 1
    for x in l[1:]:
        if x < lo or x > hi:
            return False
        lo, hi, d = x, x, -d
    return True