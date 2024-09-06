def monotonic(lst):
    if len(lst) <= 1:
        return True
    return (lst[1:] + lst[:-1]) == sorted(lst)