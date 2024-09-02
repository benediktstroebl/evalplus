
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
        return []
    new_lst = []
    lst_sort = sorted(lst)
    while lst_sort:
        new_lst.append(lst_sort.pop(0))
        if lst_sort:
            new_lst.append(lst_sort.pop(-1))
    return new_lst

