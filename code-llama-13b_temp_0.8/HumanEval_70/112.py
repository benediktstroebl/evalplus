
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
    if len(lst) == 1:
        return lst
    else:
        lst_min = min(lst)
        lst_max = max(lst)
        lst.remove(lst_min)
        lst.remove(lst_max)
        return [lst_min, lst_max] + strange_sort_list(lst)

