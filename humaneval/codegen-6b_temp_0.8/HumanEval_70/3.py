
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
    lst_len = len(lst)
    if lst_len == 0:
        return lst
    min_value = min(lst)
    strange_lst = [min_value]
    del lst[lst.index(min_value)]
    for i in range(len(lst)):
        max_v = max(lst)
        strange_lst.append(max_v)
        lst.pop(lst.index(max_v))
    strange_lst.append(min_value)
    return strange_lst

