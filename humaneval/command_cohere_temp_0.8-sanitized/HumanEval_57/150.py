def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while lo <= hi:
        if (mid == 0 or l[mid] <= l[mid - 1]) and (mid == len(l) - 1 or l[mid + 1] >= l[mid]) and (mid == 0 or l[mid] >= l[mid + 1]):
            return True
        elif l[mid] < l[mid + 1] and l[mid] <= l[mid - 1]:
            return False
        elif l[mid] > l[mid + 1] and l[mid] >= l[mid - 1]:
            return True
        elif l[mid] == l[mid + 1] and l[mid] == l[mid - 1]:
            mid = (mid + 1) // 2
            lo = mid + 1
            mid = (mid + 1) // 2
            hi = len(l) - 1
        else:
            return False
    return False