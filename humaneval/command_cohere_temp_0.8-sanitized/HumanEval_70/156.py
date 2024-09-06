def strange_sort_list(lst):
    out = [min(lst)]
    for i in lst:
        if i > out[-1]:
            out.append(i)
    return out