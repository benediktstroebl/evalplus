def monotonic(lst):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo < hi:
        if lst[mid] >= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            return True
        elif lst[mid] < lst[mid - 1] and lst[mid + 1] < lst[mid]:
            return True
        elif lst[mid] >= lst[mid + 1] and lst[mid] <= lst[mid - 1]:
            return False
        elif lst[mid] < lst[mid + 1] and lst[mid] >= lst[mid - 1]:
            return False
        lo += 1
        hi -= 1
        mid += 1
    return False