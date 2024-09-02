
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
    res = []
    lst_cpy = lst.copy()
    lst_min = min(lst)
    res.append(lst_min)
    lst_cpy.remove(lst_min)

    while lst_cpy:
        lst_max = max(lst_cpy)
        res.append(lst_max)
        lst_cpy.remove(lst_max)

        lst_min = min(lst_cpy)
        res.append(lst_min)
        lst_cpy.remove(lst_min)

    return res
