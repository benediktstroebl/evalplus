
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
    min_num = min(lst)
    max_num = max(lst)
    if min_num == max_num:
        return lst
    res = []
    while lst:
        res.append(min_num)
        lst.remove(min_num)
        if lst:
            res.append(max_num)
            lst.remove(max_num)
    return res
