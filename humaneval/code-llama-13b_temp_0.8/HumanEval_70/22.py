
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
    res.append(min(lst))
    while len(res) < len(lst):
        res.append(max(lst))
        lst.remove(max(lst))
        res.append(min(lst))
        lst.remove(min(lst))
    return res
    
