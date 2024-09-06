
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
        return lst
    new_lst = []
    for i in range(1, len(lst) + 1):
        if i == 1:
            new_lst.append(min(lst))
        if i == len(lst):
            new_lst.append(max(lst))
        if i > 1 and i < len(lst):
            new_lst.append(min(lst[i:]))
            lst.remove(min(lst[i:]))
    return new_lst
