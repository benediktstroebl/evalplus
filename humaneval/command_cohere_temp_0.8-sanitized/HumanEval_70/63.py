def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for x in lst if x != min(lst)]
        if len(out) > 1 and out[-2] == out[-1]:
            out.pop()
        else:
            max_idx = out.append(max(lst))
            lst = [x for x in lst if x != max(lst)]
    return out