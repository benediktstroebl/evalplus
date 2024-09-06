def strange_sort_list(lst):
    # Sort the list, but always keep the minimum value at the first position
    if len(lst) == 0:
        return lst
    return [min(lst)] + [max(lst[:-1]) for _ in range(len(lst) - 2)]