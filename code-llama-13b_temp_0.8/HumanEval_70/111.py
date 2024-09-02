
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
    lst_len = len(lst)
    if lst_len % 2 == 0:
        while lst:
            # first loop
            res.append(min(lst))
            lst.remove(min(lst))
            # second loop
            res.append(max(lst))
            lst.remove(max(lst))
    else:
        while lst:
            # first loop
            res.append(min(lst))
            lst.remove(min(lst))
            # second loop
            res.append(max(lst))
            lst.remove(max(lst))
            # third loop
            res.append(min(lst))
            lst.remove(min(lst))
    return res

