def monotonic(lst):
    if len(lst) <= 1:
        return True
    if lst[1] < lst[0]:
        return monotonic(lst[1:]) and True
    if lst[1] > lst[0]:
        return monotonic(lst[:-1]) and False
    else:
        return monotonic(lst[1:]) or monotonic(lst[:-1])