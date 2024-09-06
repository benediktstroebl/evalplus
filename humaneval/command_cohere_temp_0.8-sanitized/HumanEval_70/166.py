def strange_sort_list(lst):
    out = [min(lst)]
    for x in lst:
        if x > out[-1]:
            out.append(x)
    return out