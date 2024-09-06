def strange_sort_list(lst):
    # Sort the list, but always keep the minimum and maximum element in their respective places.
    # Then remove the element that is no longer needed (min or max).
    if not lst:
        return lst
    min_val = min(lst)
    max_val = max(lst)
    min_idx = lst.index(min_val)
    max_idx = lst.index(max_val)
    middle_val = lst[0] if min_idx == 0 else lst[1]