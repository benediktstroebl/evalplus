def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, d = float('-inf'), float('inf'), 1
    for x in l[1:]:
        if x < lo or x > hi:
            return False
        if x > lo:
            lo = x
        if x < hi:
            hi = x
        d += 1
        if d > 2:  # to avoid potential infinite loop
            return True
    return False