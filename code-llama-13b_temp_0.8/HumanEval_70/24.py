
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
    if not lst:
        return lst
    res = []
    lst_len = len(lst)
    for idx in range(lst_len // 2 + lst_len % 2):
        if idx == 0:
            res.append(min(lst))
        else:
            if idx % 2 == 1:
                res.append(max(lst))
            else:
                res.append(min(lst))
        lst.remove(res[-1])
    return res













