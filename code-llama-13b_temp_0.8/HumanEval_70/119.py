
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
    l = lst[:]
    for _ in range(len(l)):
        res.append(min(l))
        l.remove(min(l))
        if l:
            res.append(max(l))
            l.remove(max(l))
    return res

