def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo < hi:
        if lst[mid] <= lst[mid + 1]:
            if mid == 0 or lst[mid] >= lst[lo]:
                lo = mid + 1
            else:
                return False
        else:
            if mid == len(lst) - 1 or lst[mid] <= lst[hi]:
                hi = mid
            else:
                return False
        mid = (lo + hi) // 2
    return True