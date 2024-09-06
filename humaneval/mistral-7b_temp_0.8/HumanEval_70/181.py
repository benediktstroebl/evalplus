
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
    min_v = min(lst)
    max_v = max(lst)
    if max_v == min_v:
        return lst
    lst_r = lst.copy()
    for i in lst:
        if i < min_v:
            min_v = i
        elif i > max_v:
            max_v = i
    lst_r.remove(min_v)
    lst_r.remove(max_v)
    return [min_v, max_v] + lst_r
