def strange_sort_list(lst):
    # Sort the list in a strange way as per the specification
    strange = []
    available = lst
    while available:
        min_idx = available.index(min(available))
        strange.append(available[min_idx])
        available.remove(available[min_idx])
    return strange + available