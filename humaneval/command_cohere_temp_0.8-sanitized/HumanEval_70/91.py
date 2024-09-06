def strange_sort_list(lst):
    min_idx = 0
    sorted_idx = [0]
    for i in range(1, len(lst)):
        if lst[i] < lst[min_idx]:
            min_idx = i
        elif lst[i] > lst[sorted_idx[0]]:
            sorted_idx[0] = i
    sorted_lst = [lst[min_idx]]
    for idx in sorted_idx:
        sorted_lst.append(lst[idx])
    return sorted_lst