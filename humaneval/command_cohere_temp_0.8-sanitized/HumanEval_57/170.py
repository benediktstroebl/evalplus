def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo < hi:
        if lst[mid] >= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo < len(lst) - 1 and lst[lo] <= lst[-1]