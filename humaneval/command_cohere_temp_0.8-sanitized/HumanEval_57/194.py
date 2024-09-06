def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
        mid = (hi + lo) // 2
    return True if (hi >= 0 and l[hi] <= l[hi + 1]) or (lo >= 0 and l[lo] >= l[lo + 1]) else False