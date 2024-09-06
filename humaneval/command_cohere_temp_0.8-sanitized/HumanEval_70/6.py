def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i,x in enumerate(lst) if i != min_idx]
        if len(lst) == 1: break
        max_idx = out.append(max(lst))
        lst = [x for i,x in enumerate(lst) if i != max_idx]
    return out