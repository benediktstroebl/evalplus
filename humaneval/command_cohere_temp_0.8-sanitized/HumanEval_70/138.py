def strange_sort_list(lst):
    min_idx = 0
    max_idx = 0
    sorted_list = [min(lst)]
    for idx, num in enumerate(lst):
        if num > lst[max_idx]:
            max_idx = idx
        elif num < lst[min_idx]:
            min_idx = idx
        elif idx > max_idx:
            sorted_list.append(lst[idx])
    return sorted_list