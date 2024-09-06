
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
    max_val = max(lst)
    min_val = min(lst)
    res.append(min_val)
    if len(lst) > 1:
        lst.remove(min_val)
        res.append(max(lst))
        lst.remove(max(lst))
        for i in lst:
            if i == max_val:
                res.append(min(lst))
                lst.remove(min(lst))
            elif i == min_val:
                res.append(max(lst))
                lst.remove(max(lst))
    return res
