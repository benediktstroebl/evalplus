def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for x in lst if x != min(lst)]
        if len(out) > 1 and out[-2] == min(lst):
            out.pop()
            out.append(max(lst))
            lst = [x for x in lst if x != max(lst)]
        if len(out) > 1 and out[-1] == min(lst):
            out.pop()
    return out