
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
    if lst_len < 2:
        return lst

    min_val = lst[0]
    max_val = lst[0]
    for val in lst[1:]:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    return strange_sort_list([min_val]) + [max_val] + strange_sort_list(
        [v for v in lst if v not in (min_val, max_val)]
    )
