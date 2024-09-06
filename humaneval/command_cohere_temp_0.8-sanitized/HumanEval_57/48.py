def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo <= hi:
        if lst[mid] >= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            return True
        elif lst[mid] <= lst[mid - 1]:
            lo = mid + 1
        elif lst[mid] >= lst[mid + 1]:
            hi = mid - 1
        else:
            return False
        mid = (lo + hi) // 2
    return False