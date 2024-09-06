def monotonic(lst):
    if len(lst) <= 1:
        return True
    else:
        return lst[1:] == lst[0: len(lst) - 1] or lst[1:] == lst[2: len(lst)]