def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = len(lst) - lst[:len(lst)].index(min(lst)) - 1
        out.append(lst.pop(min_idx))
        if len(lst) == 1:
            break
    return out