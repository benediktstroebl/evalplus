def monotonic(lst):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while hi - lo > 1:
        if lst[mid] < lst[mid - 1] and lst[mid] < lst[mid + 1]:
            return True
        elif lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return True
        elif lst[mid] == lst[mid - 1] and lst[mid] == lst[mid + 1]:
            return True
        lo = mid
        mid = (lo + hi) // 2
        hi = mid + 1
    return lst[mid] == lst[mid - 1] or lst[mid] == lst[mid + 1]