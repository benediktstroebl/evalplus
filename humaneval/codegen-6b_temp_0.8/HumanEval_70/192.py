
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
    res = []
    min_num = min(lst)
    max_num = max(lst)
    lst.remove(min_num)
    res.append(min_num)
    for i in range(len(lst)):
        res.append(max_num)
        max_num = max(lst)
        lst.remove(max_num)
    res.append(max_num)
    return res
