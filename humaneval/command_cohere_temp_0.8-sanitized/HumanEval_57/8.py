def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[lo] and l[mid] <= l[hi]:
            return True
        elif l[mid] >= l[lo] and l[mid] >= l[hi]:
            return True
        elif l[hi] >= l[mid] < l[lo]:
            return False
        elif l[hi] <= l[mid] and l[mid] < l[lo]:
            return True
        elif l[lo] < l[mid] < l[hi]:
            return True
        lo = mid
        mid = (hi + lo) // 2
        hi = mid
    return l[mid] <= l[hi] or l[mid] >= l[lo]