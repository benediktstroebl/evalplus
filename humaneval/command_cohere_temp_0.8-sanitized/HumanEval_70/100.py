def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i,x in enumerate(lst) if i != min_idx]
    return out