def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.index(min(lst)) + 1 if result else 0
        result.append(lst.pop(min_idx))
    return result