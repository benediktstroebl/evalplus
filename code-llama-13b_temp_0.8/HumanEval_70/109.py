
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
    if len(lst) == 0:
        return res
    max_lst = [x for x in lst if x >= lst[0]]
    min_lst = [x for x in lst if x <= lst[0]]
    for i in range(len(lst)):
        if i % 2 == 0:
            res.append(min_lst.pop(0))
        else:
            res.append(max_lst.pop(-1))
    return res

