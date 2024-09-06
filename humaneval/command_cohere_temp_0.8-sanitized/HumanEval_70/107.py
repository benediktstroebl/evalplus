def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.append(min(lst))
        lst = [x for i, x in enumerate(lst) if i != min_idx]
        if not lst:
            break
        result.append(max(lst))
        lst = [x for x in lst if x != max(lst)]
    return result