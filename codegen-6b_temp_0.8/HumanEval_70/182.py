
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
    lst_n = []
    lst_m = []
    min_val = min(lst)
    while lst != []:
        if lst[0] == min_val:
            lst_n.append(lst[0])
            lst.pop(0)
        else:
            lst_m.append(max(lst))
            lst.remove(max(lst))
    lst_m.append(min_val)
    return lst_n + lst_m
