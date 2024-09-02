
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
    lst_new = []
    while len(lst) > 1:
        min_ = min(lst)
        lst.remove(min_)
        max_ = max(lst)
        lst.remove(max_)
        lst_new.append(min_)
        lst_new.append(max_)
    lst_new.append(lst[0])
    return lst_new
