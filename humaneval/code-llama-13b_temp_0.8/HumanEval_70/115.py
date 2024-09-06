
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
    list_len = len(lst)
    if list_len == 0:
        return lst

    res = []
    while len(res) != list_len:
        temp = min(lst)
        lst.remove(temp)
        res.append(temp)
        if len(lst) > 0:
            temp = max(lst)
            lst.remove(temp)
            res.append(temp)

    return res

