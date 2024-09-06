def strange_sort_list(lst):
    # Sort the list alternatively using `min` and `max` on the remaining values
    return [min(lst[1:]) if len(lst) > 1 else lst[0],
            max(lst[1:]) if len(lst) > 1 else lst[0],
            min(lst[2:]) if len(lst) > 2 else lst[1],
            max(lst[2:]) if len(lst) > 2 else lst[1]
            ]