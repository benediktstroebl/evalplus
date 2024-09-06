def strange_sort_list(lst):
    # Ensure list is sorted in descending order and contains at least two elements
    if len(lst) < 2:
        return lst
    min_val = min(lst)
    max_val = max(lst)
    return [min_val] + [max_val] + strange_sort_list(lst[:-2])