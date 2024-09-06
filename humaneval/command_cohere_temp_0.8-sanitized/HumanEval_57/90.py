def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while lo < hi:
        if l[mid] <= l[mid + 1]:
            if mid == 0 or l[mid - 1] < l[mid]:
                hi = mid + 1
            else:
                lo = mid + 1
        else:
            if mid == len(l) - 1 or l[mid + 1] < l[mid]:
                lo = mid + 1
            else:
                hi = mid + 1
        mid = (lo + hi) // 2
    return lo < len(l)