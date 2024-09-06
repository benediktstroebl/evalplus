def monotonic(lst):
    if len(lst) <= 1:
        return True
    else:
        if lst[1] >= lst[0]:
            return monotonic(lst[1:])
        else:
            return monotonic(lst[:-1])