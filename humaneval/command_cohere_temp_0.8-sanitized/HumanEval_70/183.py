def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for x in lst if x > lst[min_idx]]
    return out