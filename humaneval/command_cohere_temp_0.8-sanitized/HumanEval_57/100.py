def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while hi - lo > 1:
        if lst[mid] <= lst[mid + 1]:
            if lst[lo] <= lst[mid] and lst[mid] <= lst[hi]:
                return True
            mid = (lo + hi) // 2
            lo = mid
        else:
            if lst[lo] <= lst[mid] and lst[mid] <= lst[hi]:
                return True
            hi = mid
    return lst[lo] <= lst[hi]