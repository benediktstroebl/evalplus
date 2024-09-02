
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

    if len(lst) < 2:
        return lst
    new_lst = sorted(lst)
    new_lst[0], new_lst[-1] = new_lst[-1], new_lst[0]
    return strange_sort_list(new_lst[1: -1]) + [new_lst[0]]
