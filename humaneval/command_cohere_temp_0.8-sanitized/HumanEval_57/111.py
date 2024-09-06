def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, len(lst) - 1, int((len(lst) + 1) / 2)
    if lst[mid] < lst[mid - 1] and lst[mid] < lst[mid + 1]:
        return True
    if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
        return True
    if lst[mid] == lst[mid - 1] and lst[mid] == lst[mid + 1]:
        return monotonic(lst[mid - 1 : mid + 2] + lst[mid : mid - 1] + lst[mid + 2 :])
    return monotonic(lst[:mid] + lst[mid + 1:]) or monotonic(lst[mid:] + lst[:mid - 1])