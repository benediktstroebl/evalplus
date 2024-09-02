
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
    sort_lst = []
    while lst:
        min_val = min(lst)
        sort_lst.append(min_val)
        lst.remove(min_val)
        if len(lst) > 1:
            max_val = max(lst)
            sort_lst.append(max_val)
            lst.remove(max_val)
    return sort_lst
