def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = len(lst)
        for i, num in enumerate(lst):
            if num < lst[min_idx]:
                min_idx = i
        out.append(lst.pop(min_idx))
        if len(lst) > 1:
            max_idx = len(lst)
            for i, num in enumerate(lst):
                if num > lst[max_idx]:
                    max_idx = i
            out.append(lst.pop(max_idx))
    return out