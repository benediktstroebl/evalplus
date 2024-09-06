
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
    if not lst:
        return []
    new_lst = []
    new_lst.append(min(lst))
    lst.remove(min(lst))
    while lst:
        min_index = min(lst)
        new_lst.append(max(lst))
        lst.remove(max(lst))
        new_lst.append(min_index)
        lst.remove(min_index)
    return new_lst
