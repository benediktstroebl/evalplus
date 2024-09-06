
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

    if len(lst) == 0:
        return []
    else:
        lst_strange = []
        new_lst = lst[:]
        min = min(new_lst)
        new_lst.remove(min)
        lst_strange.append(min)
        max = max(new_lst)
        new_lst.remove(max)
        lst_strange.append(max)
        return lst_strange + strange_sort_list(new_lst)

