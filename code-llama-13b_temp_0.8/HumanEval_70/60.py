
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
    tmp = list(lst)
    while len(tmp) > 0:
        res.append(min(tmp))
        tmp.remove(min(tmp))
        if len(tmp) > 0:
            res.append(max(tmp))
            tmp.remove(max(tmp))
    return res

