def strange_sort_list(lst):
    min_idx = 0
    sorted_lst = [min(lst)]
    for i in range(1, len(lst)):
        if lst[i] > lst[min_idx]:
            min_idx = i
            sorted_lst.append(lst[i])
        elif lst[i] < lst[min_idx]:
            sorted_lst.append(lst[min_idx])
    return sorted_lst