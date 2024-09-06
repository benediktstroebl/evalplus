def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.append(min(lst))
        lst = [x for i, x in enumerate(lst) if i != min_idx]
        if not lst:
            break
        max_idx = result.append(max(lst))
        lst = [x for i, x in enumerate(lst) if i != max_idx]
    return result