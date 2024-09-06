def strange_sort_list(lst):
    """
    Do a strange sort of the list, return it in order
    Strangely sorted list: arranges values in increasing order, 
    but always skips the lowest value in the sequence
    """
    res = []
    seen = []
    for i in lst:
        if i < max(seen) and i != min(lst):
            res.append(i)
            seen.append(i)
    return res