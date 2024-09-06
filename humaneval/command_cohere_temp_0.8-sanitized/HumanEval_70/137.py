def strange_sort_list(lst):
    result = []
    while lst:
        min_val = min(lst)
        max_rem = max(x for x in lst if x > min_val)
        result.extend([min_val, max_rem])
        lst = [x for x in lst if x <= max_rem]
    return result