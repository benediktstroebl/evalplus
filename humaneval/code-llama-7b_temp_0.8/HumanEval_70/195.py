
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
    lst_len = len(lst)
    if lst_len == 0:
        return []
    ret = []
    lst_min = min(lst)
    lst_max = max(lst)
    while len(lst) > 0:
        if len(lst) == 1:
            ret.append(lst[0])
            lst.pop()
        elif lst[0] == lst_min:
            ret.append(lst_max)
            lst.pop()
            lst_max = max(lst)
        elif lst[0] == lst_max:
            ret.append(lst_min)
            lst.pop()
            lst_min = min(lst)
        else:
            ret.append(lst[0])
            lst.pop()
            lst_min = min(lst)
            lst_max = max(lst)
    return ret
