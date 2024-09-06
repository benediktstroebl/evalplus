def monotonic(lst):
    if len(lst) <= 1:
        return True
    elif lst[1] >= lst[0] or lst[-2] <= lst[-1]:
        return True
    else:
        return False