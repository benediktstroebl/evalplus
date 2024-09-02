
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
    if lst == []:
        return lst
    min_lst = []
    max_lst = []
    lst_copy = lst.copy()
    lst_len = len(lst_copy)
    i = 0
    while i < lst_len:
        min_lst.append(min(lst_copy))
        lst_copy.remove(min(lst_copy))
        i += 1
    i = 0
    while i < lst_len:
        max_lst.append(max(lst_copy))
        lst_copy.remove(max(lst_copy))
        i += 1
    res = min_lst + max_lst
    return res

