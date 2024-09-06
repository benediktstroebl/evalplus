def strange_sort_list(lst):
    # sort values and retain position by toggling between min and max values
    seen = []
    result = []
    while lst:
        min_val = min(lst)
        max_idx = lst.index(max(lst))
        result.append(min_val)
        lst[max_idx] = min(lst)
        seen.append(min_val)
        lst = [v for v in lst if v not in seen]
    return result