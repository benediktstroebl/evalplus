def next_smallest(lst):
    if len(lst) < 2:
        return None
    mn = min(lst)
    ng = None
    for n in lst:
        if n > mn and (ng is None or n < ng):
            ng = n
    return ng