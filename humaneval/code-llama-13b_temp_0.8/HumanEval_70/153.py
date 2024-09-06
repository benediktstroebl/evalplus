
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
    if len(lst) < 1:
        return lst
    min_el = min(lst)
    max_el = max(lst)
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] = min_el
        else:
            lst[i] = max_el
        lst = sorted(lst)
    return lst

