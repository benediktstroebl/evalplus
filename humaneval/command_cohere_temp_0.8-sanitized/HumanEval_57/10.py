def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, len(lst) - 1, (lo + hi) // 2
    if lst[mid] > lst[mid + 1] or lst[mid] < lst[mid - 1]:
        return False
    else:
        if lst[mid] <= lst[mid + 1] and lst[mid] >= lst[mid - 1]:
            return monotonic(lst[:mid] + lst[mid + 1:]) and monotonic(lst[mid:] + lst[:mid + 1])
        else:
            return monotonic(lst[:mid]) or monotonic(lst[mid:])