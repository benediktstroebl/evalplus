
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
        tmp = min(lst)
        lst.remove(tmp)
        res.append(tmp)
        if lst:
            tmp = max(lst)
            lst.remove(tmp)
            res.append(tmp)
    return res

