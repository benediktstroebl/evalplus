def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    lo, hi = 0, len(lst) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] == lst[mid + 1]:
            return lst[mid]
        elif lst[mid] > lst[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return None