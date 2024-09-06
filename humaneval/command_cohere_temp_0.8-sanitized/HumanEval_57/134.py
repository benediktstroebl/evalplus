def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[mid + 1]:
            if mid == 0 or l[mid - 1] < l[mid]:
                hi = mid
            else:
                return False
        elif l[mid] >= l[mid + 1]:
            if mid == len(l) - 1 or l[mid + 1] > l[mid]:
                lo = mid
            else:
                return False
        mid = (hi + lo) // 2
    return True