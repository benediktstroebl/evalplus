
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
    new_lst = []
    len_lst = len(lst)
    while len(lst):
        if not new_lst:
            new_lst.append(min(lst))
        else:
            new_lst.append(max(lst))
        lst.remove(min(lst))
        if len(lst) == len_lst:
            lst.remove(max(lst))
            new_lst.append(min(lst))
        len_lst -= 1
    return new_lst

