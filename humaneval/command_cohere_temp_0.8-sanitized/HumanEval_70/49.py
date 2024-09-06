def strange_sort_list(lst):
    out = []
    n = len(lst)
    if n == 0:
        return lst
    min_val = min(lst)
    max_remaining = max(lst[:n-1])
    out.append(min_val)
    out.append(max_remaining)
    out.extend(strange_sort_list(lst[n-2:]))
    return out