
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
    while lst:
        if len(lst) == 1:
            res.append(lst[0])
            lst.remove(lst[0])
        elif len(lst) == 2:
            res.append(min(lst))
            res.append(max(lst))
            lst = []
        else:
            res.append(min(lst))
            lst.remove(min(lst))
            res.append(max(lst))
            lst.remove(max(lst))
    return res
