
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
    min_val = min(lst)
    max_val = max(lst)
    lst_len = len(lst)
    if lst_len == 1:
        return lst
    elif min_val == max_val:
        return lst
    elif lst_len == 2:
        return [lst[1], lst[0]]
    else:
        return [min_val] + [max_val] + strange_sort_list(lst[2:lst_len])
