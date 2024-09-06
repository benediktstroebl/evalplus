def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, len(lst) - 1, (lo + hi) // 2
    if lst[mid] > lst[mid + 1]:
        return monotonic(lst[mid + 1:]) and monotonic(lst[:mid])
    if lst[mid] < lst[mid + 1]:
        return monotonic(lst[:mid]) and monotonic(lst[mid + 1:])
    return monotonic(lst[mid + 1:]) or monotonic(lst[:mid])