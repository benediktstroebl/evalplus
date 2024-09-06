def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]