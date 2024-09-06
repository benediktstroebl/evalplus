def strange_sort_list(lst):
    min_idx = 0
    max_idx = 0
    sorted_list = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > lst[max_idx]:
            max_idx = i
        elif lst[i] < lst[min_idx]:
            min_idx = i
        else:
            pass
    for i in range(len(lst) - 2, -1, -1):
        sorted_list.append(lst[i])
    return sorted_list