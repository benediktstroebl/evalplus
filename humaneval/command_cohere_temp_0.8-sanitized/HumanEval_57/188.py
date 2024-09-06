def monotonic(lst):
    if len(lst) <= 1:
        return True
    elif lst[1] >= lst[0]:
        return monotonic(lst[1:])
    elif lst[1] <= lst[0]:
        return monotonic(lst[:-1])
    else:
        return False