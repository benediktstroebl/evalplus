def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while lo <= hi:
        if (mid == 0 or l[mid] <= l[mid - 1]) and (mid == len(l) - 1 or l[mid + 1] >= l[mid]) and (lo == 0 or l[lo] <= l[mid - 1]) and (hi == len(l) - 1 or l[hi] >= l[mid + 1]):
            return True
        elif l[mid] <= l[mid - 1] and l[mid + 1] < l[mid]:
            lo = mid + 1
        elif l[mid] < l[mid + 1] and l[mid - 1] <= l[mid]:
            hi = mid - 1
        else:
            mid = (lo + hi) // 2
    return False