def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi = l[0], l[-1]
    for i in range(1, len(l)-1):
        if (hi < l[i] < lo) or (lo < l[i] < hi):
            return False
        if l[i] == lo and l[i] == hi:
            return False
        lo, hi = hi, l[i]
    return True