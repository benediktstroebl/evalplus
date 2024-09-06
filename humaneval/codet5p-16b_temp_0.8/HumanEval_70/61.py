
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
        return []
    sorted_lst = sorted(lst)
    strange_order = []
    while sorted_lst:
        strange_order.append(min(sorted_lst))
        sorted_lst.remove(min(sorted_lst))
        if len(sorted_lst)!= 0:
            strange_order.append(max(sorted_lst))
            sorted_lst.remove(max(sorted_lst))
        if len(sorted_lst) == 0:
            break
    return strange_order
