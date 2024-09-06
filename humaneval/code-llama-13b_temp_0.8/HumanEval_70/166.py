
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
    lst_tmp = lst[:]
    new_lst = []
    while len(lst_tmp) > 0:
        minimum = min(lst_tmp)
        new_lst.append(minimum)
        lst_tmp.remove(minimum)
        if lst_tmp:
            maximum = max(lst_tmp)
            new_lst.append(maximum)
            lst_tmp.remove(maximum)
    return new_lst

