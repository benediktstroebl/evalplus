def strange_sort_list(lst):
    # Sort the list, but always keep the minimum value at the first position
    if len(lst) == 0:
        return lst
    min_val = min(lst)
    max_except_min = max(x for x in lst if x != min_val)
    return [min_val, max_except_min, strange_sort_list(lst[:len(lst) - 1])]