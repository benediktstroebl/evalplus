def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while hi - lo > 1:
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return True
        elif lst[mid] < lst[mid - 1] and lst[mid] < lst[mid + 1]:
            return True
        elif lst[mid] == lst[mid - 1] and lst[mid] == lst[mid + 1]:
            return True
        elif lst[mid] <= lst[mid + 1]:
            lo = mid
        else:
            hi = mid
        mid = (hi + lo) // 2
    return lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]