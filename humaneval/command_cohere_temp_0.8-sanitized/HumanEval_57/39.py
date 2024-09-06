def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[mid + 1]:
            if l[mid] <= l[lo] or l[mid + 1] >= l[hi]:
                return True
            mid += 1
        else:
            if l[mid] >= l[mid - 1] or l[lo] >= l[mid]:
                return True
            lo += 1
    return l[mid] <= l[mid + 1] and monotonic(l[:mid]) or \
        l[mid] >= l[mid + 1] and monotonic(l[mid + 1:])