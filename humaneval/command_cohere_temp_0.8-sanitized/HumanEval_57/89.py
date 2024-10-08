def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] < l[mid - 1] and l[mid] < l[mid + 1]:
            return True
        elif l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
            return True
        elif l[mid] == l[mid - 1] and l[mid] == l[mid + 1]:
            return False
        lo = mid
        mid = (lo + hi) // 2
        hi = mid + 1
    return l[mid] == l[mid - 1] or l[mid] == l[mid + 1]