def strange_sort_list(lst):
    result = []
    while len(lst) > 0:
        min_idx = result.index(min(result)) if len(result) > 0 else len(lst) - 1
        max_idx = result.index(max(lst)) if len(lst) > 0 else -1
        result.insert(min_idx, lst.pop(max_idx))
    return result