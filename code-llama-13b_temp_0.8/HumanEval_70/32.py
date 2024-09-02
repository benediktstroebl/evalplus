
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
    lst_copy = lst[:]
    while lst_copy:
        min_val = min(lst_copy)
        max_val = max(lst_copy)
        res.append(min_val)
        res.append(max_val)
        lst_copy.remove(min_val)
        lst_copy.remove(max_val)
    return res

