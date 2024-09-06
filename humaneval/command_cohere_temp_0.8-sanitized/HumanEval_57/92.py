def monotonic(lst):
    if len(lst) <= 1:
        return True
    if lst[1] < lst[0]:
        return monotonic(lst[1:]) and not (lst[2] < lst[1])
    if lst[1] > lst[0]:
        return not (lst[0] > lst[1:][0]) and monotonic(lst[1:])
    return False