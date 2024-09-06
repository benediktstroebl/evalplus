def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, d = l[0], l[-1], l[0] - l[-1]
    for i in range(1, len(l)-1):
        if l[i] > hi or l[i] < lo:
            return False
        if l[i] == lo and l[i+1] == lo:
            return False
        if l[i] == hi and l[i-1] == hi:
            return False
        if l[i]-l[i-1] != d:
            return False
        lo, hi, d = l[i], hi, l[i]-l[i-1]
    return True