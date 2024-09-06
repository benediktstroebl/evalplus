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
        elif l[hi] < l[mid] < l[lo]:
            return True
        elif l[hi] > l[mid] > l[lo]:
            return True
        else:
            return False
        mid = (hi + lo) // 2
        lo = mid
        hi = mid
    return l[mid] <= l[hi] and l[mid] <= l[lo] or l[mid] >= l[hi] and l[mid] >= l[lo]