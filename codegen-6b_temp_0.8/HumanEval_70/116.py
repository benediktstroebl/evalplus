
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if lst == []:
        return []
    min_num = min(lst)
    max_num = max(lst)
    strange_lst = []
    for i in range(len(lst)):
        if lst[i] == min_num:
            strange_lst.append(max_num)
            strange_lst.append(min_num)
        elif lst[i] == max_num:
            strange_lst.append(min_num)
            strange_lst.append(max_num)
        else:
            strange_lst.append(lst[i])
    return strange_lst
